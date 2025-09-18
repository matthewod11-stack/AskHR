from __future__ import annotations
import csv, json, time, os
from typing import Iterable, List, Tuple, Dict, Any
from dataclasses import asdict
import requests

from .schema import EvalCase, EvalResult, EvalSummary

def load_cases(csv_path: str) -> List[EvalCase]:
    cases: List[EvalCase] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            cases.append(EvalCase.from_row(row))
    return cases

def tokenize_len(text: str) -> int:
    # Simple proxy for tokens: whitespace split
    if not text:
        return 0
    return len(text.split())

def extract_citation_paths(citations: Any) -> List[str]:
    """
    Be generous in what we accept:
    - list[str]
    - list[dict] with a 'source_path' or 'path' field
    - list[dict[str, str]] arbitrary keys containing something path-like
    """
    paths: List[str] = []
    if isinstance(citations, list):
        for item in citations:
            if isinstance(item, str):
                paths.append(item)
            elif isinstance(item, dict):
                # preferred fields
                for key in ("source_path","path","source","file","location"):
                    if key in item and isinstance(item[key], str):
                        paths.append(item[key])
                        break
                else:
                    # as a fallback, stringify
                    paths.append(json.dumps(item, ensure_ascii=False))
    return paths

def any_expected_hit(answer: str, paths: List[str], expects: List[str]) -> Tuple[bool, int]:
    if not expects:
        return False, 0
    haystacks = [answer or ""] + paths
    matched_cites = 0
    any_hit = False
    for e in expects:
        e_low = e.lower()
        # Count how many citations contain this expected substring
        cite_hits = sum(1 for p in paths if e_low in p.lower())
        matched_cites += cite_hits
        # Also allow answer-text hit to trigger 'hit'
        if not any_hit and any(e_low in h.lower() for h in haystacks):
            any_hit = True
    return any_hit, matched_cites

def ensure_dir(p: str) -> None:
    os.makedirs(p, exist_ok=True)

def call_api(api_url: str, case: EvalCase, timeout_s: int = 60) -> Tuple[str, List[str]]:
    payload = {
        "query": case.query,
        "k": case.k,
        "grounded_only": case.grounded_only,
    }
    url = f"{api_url.rstrip('/')}/v1/ask"
    r = requests.post(url, json=payload, timeout=timeout_s)
    r.raise_for_status()
    data = r.json()
    # try common fields
    answer = data.get("answer") or data.get("text") or ""
    citations = extract_citation_paths(data.get("citations", []))
    return answer, citations

def evaluate_cases(api_url: str, cases: List[EvalCase], limit: int = 0, save_dir: str = "eval/results") -> Tuple[List[EvalResult], EvalSummary, str, str]:
    ensure_dir(save_dir)
    ts = time.strftime("%Y%m%d-%H%M%S")
    results_path = os.path.join(save_dir, f"results-{ts}.jsonl")
    summary_path = os.path.join(save_dir, f"summary-{ts}.json")

    results: List[EvalResult] = []
    n = len(cases) if limit <= 0 else min(limit, len(cases))
    for i, case in enumerate(cases[:n], 1):
        t0 = time.time()
        status = "ok"
        error = None
        answer = ""
        citations: List[str] = []
        try:
            answer, citations = call_api(api_url, case)
        except Exception as e:
            status = "error"
            error = str(e)
        elapsed_ms = int((time.time() - t0) * 1000)

        tokens = tokenize_len(answer)
        grounded = len(citations) > 0
        hit, matched_cites = any_expected_hit(answer, citations, case.expect_any_of or [])
        denom = max(1, len(citations))
        precision_proxy = matched_cites / denom

        results.append(EvalResult(
            id=case.id,
            query=case.query,
            answer_tokens=tokens,
            citations=citations,
            grounded=grounded,
            hit=hit,
            precision_proxy=precision_proxy,
            elapsed_ms=elapsed_ms,
            status=status,
            error=error,
            meta={"k": case.k, "grounded_only": case.grounded_only, "expects": case.expect_any_of or [], "min_citations": case.min_citations}
        ))

    # Save results JSONL
    with open(results_path, "w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps(r.to_dict(), ensure_ascii=False) + "\n")

    # Compute summary
    ok = [r for r in results if r.status == "ok"]
    answered = [r for r in ok if r.answer_tokens > 0]
    grounded_rate = (sum(1 for r in ok if r.grounded) / max(1, len(ok)))
    hit_rate = (sum(1 for r in ok if r.hit) / max(1, len(ok)))
    avg_precision = (sum(r.precision_proxy for r in ok) / max(1, len(ok)))
    avg_tokens = (sum(r.answer_tokens for r in ok) / max(1, len(ok)))

    summary = EvalSummary(
        total=len(results),
        answered=len(answered),
        grounded_rate=round(grounded_rate, 3),
        hit_rate=round(hit_rate, 3),
        avg_precision_proxy=round(avg_precision, 3),
        avg_answer_tokens=round(avg_tokens, 1),
    )

    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary.to_dict(), f, ensure_ascii=False, indent=2)

    return results, summary, results_path, summary_path

def print_summary(summary: EvalSummary) -> None:
    print("\nEVAL SUMMARY")
    print(f"  total cases:        {summary.total}")
    print(f"  answered:           {summary.answered}")
    print(f"  grounded rate:      {summary.grounded_rate:.3f}")
    print(f"  hit rate (proxy):   {summary.hit_rate:.3f}")
    print(f"  avg precision proxy:{summary.avg_precision_proxy:.3f}")
    print(f"  avg answer tokens:  {summary.avg_answer_tokens:.1f}")
