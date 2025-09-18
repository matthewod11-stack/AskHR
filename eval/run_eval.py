from __future__ import annotations
import argparse, os, sys
from .utils import load_cases, evaluate_cases, print_summary

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-url", type=str, default=os.getenv("API_URL","http://localhost:8000"))
    parser.add_argument("--cases", type=str, default="eval/cases.sample.csv")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--save-dir", type=str, default="eval/results")
    parser.add_argument("--verbose", action="store_true", help="Print per-case status lines")
    args = parser.parse_args()

    cases = load_cases(args.cases)
    results, summary, results_path, summary_path = evaluate_cases(args.api_url, cases, limit=args.limit, save_dir=args.save_dir)

    if args.verbose:
        for r in results:
            print(f"[{r.id}] status={r.status} grounded={r.grounded} hit={r.hit} tokens={r.answer_tokens}")

    print_summary(summary)
    print(f"\nSaved results: {results_path}")
    print(f"Saved summary: {summary_path}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
