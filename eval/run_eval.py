
import csv
import os
import sys
import json
from datetime import datetime
from schema import EvalCase, EvalResult, EvalSummary
import argparse
import requests

RESULTS_DIR = "eval/results"

def load_cases(path, limit=None):
    cases = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            if limit and i >= limit:
                break
            cases.append(EvalCase(
                id=row["id"],
                query=row["query"],
                expect_grounded=(row.get("expect_grounded", "false").lower() in ("1","true","yes")),
                notes=row.get("notes")
            ))
    return cases

def run_eval(cases, api_url):
    results = []
    for case in cases:
        payload = {"query": case.query, "k": 8}
        try:
            resp = requests.post(api_url, json=payload, timeout=60)
            resp.raise_for_status()
            data = resp.json()
            answer = data.get("answer", "")
            citations = data.get("citations", [])
            grounded = bool(citations)
            if case.expect_grounded:
                passed = grounded
            else:
                passed = bool(answer.strip())
            result = EvalResult(
                id=case.id,
                query=case.query,
                answer=answer,
                citations=[c.get("display_name","") for c in citations],
                grounded=grounded,
                passed=passed,
                meta={}
            )
        except Exception as e:
            result = EvalResult(
                id=case.id,
                query=case.query,
                answer=f"ERROR: {e}",
                citations=[],
                grounded=False,
                passed=False,
                meta={"error": str(e)}
            )
        results.append(result)
    return results

def summarize(results):
    total = len(results)
    passed = sum(r.passed for r in results)
    failed = total - passed
    grounded_rate = sum(r.grounded for r in results) / total if total else 0.0
    return EvalSummary(total=total, passed=passed, failed=failed, grounded_rate=grounded_rate)

def write_results(results, summary, outdir):
    os.makedirs(outdir, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d-%H%M")
    # Write JSONL
    with open(os.path.join(outdir, f"results_{ts}.jsonl"), "w") as f:
        for r in results:
            f.write(r.json() + "\n")
    # Write summary
    with open(os.path.join(outdir, f"summary_{ts}.json"), "w") as f:
        f.write(summary.json(indent=2))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-url", default="http://127.0.0.1:8000/v1/ask")
    parser.add_argument("--cases", default="eval/cases.sample.csv")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--save", action="store_true")
    args = parser.parse_args()

    cases = load_cases(args.cases, limit=args.limit)
    results = run_eval(cases, api_url=args.api_url)
    summary = summarize(results)

    print(f"Total: {summary.total}, Passed: {summary.passed}, Failed: {summary.failed}, Grounded rate: {summary.grounded_rate:.2f}")

    if args.save:
        outdir = os.path.join(RESULTS_DIR)
        write_results(results, summary, outdir)
        print(f"Results written to {outdir}")

if __name__ == "__main__":
    main()
