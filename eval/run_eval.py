# eval/run_eval.py
from __future__ import annotations

import argparse
import json
import os
from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import List, Dict, Optional

import requests

# Prefer local package modules via relative imports
from .utils import load_cases

try:
    # CaseRow is required; EvalResult/EvalSummary may or may not exist in schema.py
    from .schema import CaseRow  # type: ignore
    from .schema import EvalResult as _SchemaEvalResult  # type: ignore
    from .schema import EvalSummary as _SchemaEvalSummary  # type: ignore

    _HAVE_SCHEMA_RESULT_TYPES = True
except Exception:
    # We will provide local dataclass fallbacks below.
    CaseRow = None  # type: ignore
    _SchemaEvalResult = None  # type: ignore
    _SchemaEvalSummary = None  # type: ignore
    _HAVE_SCHEMA_RESULT_TYPES = False


RESULTS_DIR = "eval/results"


# ---------------------------------------------------------------------------
# Local fallbacks (used only if schema doesn't define these types)
# ---------------------------------------------------------------------------
if not _HAVE_SCHEMA_RESULT_TYPES:

    @dataclass
    class _SchemaEvalResult:  # type: ignore
        id: str
        query: str
        answer: str
        citations: List[str]
        grounded: bool
        passed: bool
        meta: Dict[str, str] = field(default_factory=dict)

    @dataclass
    class _SchemaEvalSummary:  # type: ignore
        total: int
        passed: int
        failed: int
        grounded_rate: float


EvalResult = _SchemaEvalResult
EvalSummary = _SchemaEvalSummary


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _resolve_endpoint(api_url: str) -> str:
    """Allow either base API URL or full /v1/ask endpoint."""
    url = (api_url or "").rstrip("/")
    if url.endswith("/v1/ask"):
        return url
    return f"{url}/v1/ask"


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------


def run_eval(cases: List[CaseRow], api_url: str, kw_threshold: int = 60) -> List[EvalResult]:  # type: ignore[name-defined]
    from .utils import score_keywords

    endpoint = _resolve_endpoint(api_url)
    results: List[EvalResult] = []
    for case in cases:
        payload = {"query": case.query, "k": 8}
        try:
            resp = requests.post(endpoint, json=payload, timeout=60)
            resp.raise_for_status()
            data = (
                resp.json() if isinstance(resp.content, (bytes, bytearray)) or resp.content else {}
            )
            answer = (data or {}).get("answer", "") or ""
            raw_citations = (data or {}).get("citations", []) or []
            grounded = bool(raw_citations)
            cit_names = []
            for c in raw_citations:
                if isinstance(c, dict):
                    name = c.get("display_name") or c.get("source_path") or c.get("id") or ""
                else:
                    name = str(c)
                cit_names.append(name)
            # Keyword scoring
            kw_score = None
            if getattr(case, "keywords", None):
                kw_score = score_keywords(answer, case.keywords)
            # Pass/Fail logic
            if getattr(case, "expect_grounded", False):
                passed = grounded and (kw_score is None or kw_score >= kw_threshold)
            else:
                passed = (
                    (kw_score is not None and kw_score >= kw_threshold)
                    if kw_score is not None
                    else bool(answer.strip())
                )
            meta = {}
            if kw_score is not None:
                meta["kw_score"] = round(kw_score, 1)
            result = EvalResult(
                id=getattr(case, "id", ""),
                query=getattr(case, "query", ""),
                answer=answer,
                citations=cit_names,
                grounded=grounded,
                passed=passed,
                meta=meta,
            )
        except Exception as e:
            result = EvalResult(
                id=getattr(case, "id", ""),
                query=getattr(case, "query", ""),
                answer=f"ERROR: {e}",
                citations=[],
                grounded=False,
                passed=False,
                meta={"error": str(e)},
            )
        results.append(result)
    return results


def summarize(results: List[EvalResult]) -> EvalSummary:
    total = len(results)
    passed = sum(1 for r in results if r.passed)
    failed = total - passed
    grounded_rate = (sum(1 for r in results if r.grounded) / total) if total else 0.0
    return EvalSummary(total=total, passed=passed, failed=failed, grounded_rate=grounded_rate)


def write_results(results: List[EvalResult], summary: EvalSummary, outdir: str) -> None:
    os.makedirs(outdir, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d-%H%M")

    # JSONL for per-case results
    results_path = os.path.join(outdir, f"results_{ts}.jsonl")
    with open(results_path, "w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps(asdict(r), ensure_ascii=False) + "\n")

    # JSON summary
    summary_path = os.path.join(outdir, f"summary_{ts}.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(asdict(summary), ensure_ascii=False, indent=2))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(description="Run AskHR evaluation harness.")
    parser.add_argument(
        "--api-url",
        default="http://127.0.0.1:8000",
        help="Base API URL (e.g., http://localhost:8000). /v1/ask is appended if missing.",
    )
    parser.add_argument(
        "--cases",
        default="eval/cases.csv",
        help="Path to cases CSV with headers: id,query,expect_grounded,notes",
    )
    parser.add_argument("--limit", type=int, default=None, help="Limit number of cases loaded")
    parser.add_argument(
        "--save", action="store_true", help="Persist results and summary to eval/results"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Load cases and exit without calling the API (for CI/smoke).",
    )
    parser.add_argument(
        "--kw-threshold", type=int, default=60, help="Keyword score threshold (0-100) for pass/fail"
    )
    parser.add_argument(
        "--report", action="store_true", help="Generate HTML report alongside results"
    )
    args = parser.parse_args()

    cases = load_cases(args.cases)
    if args.limit:
        cases = cases[: args.limit]

    if args.dry_run:
        print(f"[dry-run] Loaded {len(cases)} cases from {args.cases}.")
        return

    results = run_eval(cases, api_url=args.api_url, kw_threshold=args.kw_threshold)
    summary = summarize(results)

    print(
        f"Total: {summary.total}, Passed: {summary.passed}, "
        f"Failed: {summary.failed}, Grounded rate: {summary.grounded_rate:.2f}, "
        f"Keyword threshold: {args.kw_threshold}"
    )

    outdir = RESULTS_DIR if (args.save or args.report) else None
    if outdir:
        write_results(results, summary, outdir)
        print(f"Results written to {outdir}")
        if args.report:
            ts = datetime.now().strftime("%Y%m%d-%H%M")
            report_path = os.path.join(outdir, f"report_{ts}.html")
            results_path = os.path.join(outdir, f"results_{ts}.jsonl")
            summary_path = os.path.join(outdir, f"summary_{ts}.json")
            generate_html_report(
                results, summary, report_path, results_path, summary_path, args.kw_threshold
            )
            print(f"HTML report written to {report_path}")


def generate_html_report(results, summary, report_path, results_path, summary_path, kw_threshold):
    # Inline HTML, no extra deps
    def color_row(passed):
        return "background-color:#e6ffe6;" if passed else "background-color:#ffe6e6;"

    total = summary.total
    passed = summary.passed
    failed = summary.failed
    grounded_rate = summary.grounded_rate
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(
            f"<html><head><title>Eval Report</title><style>table{{border-collapse:collapse}}td,th{{border:1px solid #ccc;padding:4px}}</style></head><body>"
        )
        f.write(f"<h2>Evaluation Report</h2>")
        f.write(
            f"<p>Total: <b>{total}</b> | Passed: <b>{passed}</b> | Failed: <b>{failed}</b> | Pass %: <b>{(100*passed/max(1,total)):.1f}</b> | Grounded rate: <b>{grounded_rate:.2f}</b> | Keyword threshold: <b>{kw_threshold}</b></p>"
        )
        f.write(
            f'<p>Results: <a href="{os.path.basename(results_path)}">JSONL</a> | <a href="{os.path.basename(summary_path)}">Summary</a></p>'
        )
        f.write(
            "<table><tr><th>ID</th><th>Expect Grounded</th><th>Grounded</th><th>KW Score</th><th>Passed</th><th>Query</th><th>Answer</th><th>Citations</th><th>Notes</th></tr>"
        )
        for r in results:
            kw_score = r.meta.get("kw_score") if hasattr(r, "meta") else None
            answer_short = r.answer[:120] + "..." if len(r.answer) > 120 else r.answer
            citations_count = len(r.citations) if hasattr(r, "citations") else 0
            f.write(
                f'<tr style="{color_row(r.passed)}"><td>{r.id}</td><td>{getattr(r, "expect_grounded", "")}</td><td>{r.grounded}</td><td>{kw_score if kw_score is not None else "—"}</td><td>{"✅" if r.passed else "❌"}</td><td>{r.query}</td><td>{answer_short}</td><td>{citations_count}</td><td>{getattr(r, "notes", "")}</td></tr>'
            )
        f.write("</table></body></html>")


if __name__ == "__main__":
    main()
