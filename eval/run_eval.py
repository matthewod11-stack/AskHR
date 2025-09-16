
import csv
import os
import sys
import json
from datetime import datetime
from tqdm import tqdm
from tabulate import tabulate
from schema import EvalCase, EvalResult, EvalSummary
from utils import normalize_text, keyword_coverage

import argparse
import requests
import time

RESULTS_DIR = "eval/results"

def load_cases(path, limit=None):
    cases = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            if limit and i >= limit:
                break
            must_have = [kw.strip() for kw in row["must_have"].split("|")]
            min_citations = int(row["min_citations"]) if row.get("min_citations") else 2
            k = int(row["k"]) if row.get("k") else 8
            cases.append({
                "id": int(row["id"]),
                "question": row["question"],
                "must_have": must_have,
                "min_citations": min_citations,
                "k": k
            })
    return cases

def post_with_retries(api_url, payload, timeout, retries):
    attempt = 0
    while attempt <= retries:
        try:
            start = time.time()
            resp = requests.post(api_url, json=payload, timeout=timeout)
            latency = int((time.time() - start) * 1000)
            resp.raise_for_status()
            return resp.json(), latency, None
        except Exception as e:
            if attempt == retries:
                return None, 0, str(e)
            time.sleep(0.5 * (2 ** attempt))
            attempt += 1

def score_coverage(answer, must_have):
    answer_norm = normalize_text(answer)
    found = sum(1 for kw in must_have if kw.lower() in answer_norm)
    return 100.0 * found / max(1, len(must_have))

def run_eval(cases, api_url, timeout, retries):
    results = []
    for case in tqdm(cases, desc="Evaluating cases"):
        payload = {"query": case["question"], "k": case["k"]}
        resp, latency, error = post_with_retries(api_url, payload, timeout, retries)
        if resp:
            answer = resp.get("answer", "")
            citations = resp.get("citations", [])
            coverage = score_coverage(answer, case["must_have"])
            citations_count = len(citations)
            pass_fail = (coverage >= 80.0) and (citations_count >= case["min_citations"])
        else:
            answer = f"ERROR: {error}"
            citations = []
            coverage = 0.0
            citations_count = 0
            pass_fail = False
        results.append({
            "id": case["id"],
            "question": case["question"],
            "answer": answer,
            "citations": citations,
            "coverage_pct": coverage,
            "citations_count": citations_count,
            "latency_ms": latency,
            "pass_fail": pass_fail,
            "min_citations": case["min_citations"],
            "must_have": case["must_have"]
        })
    return results

def summarize(results):
    n = len(results)
    avg_coverage = sum(r["coverage_pct"] for r in results) / n if n else 0.0
    pct_ge_80 = sum(r["coverage_pct"] >= 80.0 for r in results) / n * 100 if n else 0.0
    pct_ge_min_cit = sum(r["citations_count"] >= r["min_citations"] for r in results) / n * 100 if n else 0.0
    avg_latency = sum(r["latency_ms"] for r in results) / n if n else 0.0
    pct_passed = sum(r["pass_fail"] for r in results) / n * 100 if n else 0.0
    pct_ans_ge_2_cit = sum(r["citations_count"] >= 2 for r in results) / n * 100 if n else 0.0
    acceptance = (pct_passed >= 80.0) and (pct_ans_ge_2_cit >= 90.0)
    return {
        "avg_coverage_pct": avg_coverage,
        "pct_cases_ge_80pct_coverage": pct_ge_80,
        "pct_cases_ge_min_citations": pct_ge_min_cit,
        "avg_latency_ms": avg_latency,
        "pct_cases_passed": pct_passed,
        "pct_answers_ge_2_citations": pct_ans_ge_2_cit,
        "acceptance": acceptance
    }

def write_results(cases, results, summary, outdir):
    os.makedirs(outdir, exist_ok=True)
    # Write cases used
    with open(os.path.join(outdir, "cases_used.csv"), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id","question","must_have","min_citations","k"])
        for c in cases:
            writer.writerow([c["id"], c["question"], "|".join(c["must_have"]), c["min_citations"], c["k"]])
    # Write per-case results
    with open(os.path.join(outdir, "per_case.csv"), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id","coverage_pct","citations_count","latency_ms","pass_fail"])
        for r in results:
            writer.writerow([r["id"], f"{r['coverage_pct']:.1f}", r["citations_count"], r["latency_ms"], r["pass_fail"]])
    # Write summary
    with open(os.path.join(outdir, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-url", default="http://localhost:8000/v1/ask")
    parser.add_argument("--cases", default="eval/cases.csv")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--save", action="store_true")
    parser.add_argument("--timeout", type=int, default=60)
    parser.add_argument("--retries", type=int, default=2)
    args = parser.parse_args()

    cases = load_cases(args.cases, limit=args.limit)
    results = run_eval(cases, api_url=args.api_url, timeout=args.timeout, retries=args.retries)
    summary = summarize(results)

    print(tabulate([
        [r["id"], f"{r['coverage_pct']:.1f}", r["citations_count"], r["latency_ms"], r["pass_fail"]]
        for r in results
    ], headers=["id","coverage_pct","citations_count","latency_ms","pass_fail"], tablefmt="github"))
    print("\nSummary:")
    print(tabulate([[
        f"{summary['avg_coverage_pct']:.1f}",
        f"{summary['pct_cases_ge_80pct_coverage']:.1f}",
        f"{summary['pct_cases_ge_min_citations']:.1f}",
        f"{summary['avg_latency_ms']:.1f}",
        f"{summary['pct_cases_passed']:.1f}",
        f"{summary['pct_answers_ge_2_citations']:.1f}",
        summary['acceptance']
    ]], headers=["avg_coverage_pct","pct_cases_≥80pct_coverage","pct_cases_≥min_citations","avg_latency_ms","pct_cases_passed","pct_answers_≥2_citations","acceptance"], tablefmt="github"))

    if args.save:
        ts = datetime.now().strftime("%Y%m%d-%H%M")
        outdir = os.path.join(RESULTS_DIR, ts)
        write_results(cases, results, summary, outdir)
        print(f"Results saved to {outdir}")

    # Print acceptance and set exit code
    if summary["acceptance"]:
        print("ACCEPTANCE: PASS")
        sys.exit(0)
    else:
        print("ACCEPTANCE: FAIL")
        sys.exit(2)

if __name__ == "__main__":
    main()
