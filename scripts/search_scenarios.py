import os
import argparse
import requests
import sys

API_URL = os.getenv("API_URL", "http://localhost:8000")

SCENARIOS = {
    "Attrition": [
        {"name": "Eng-only follow-up", "last_user": "show attrition by department", "last_assistant": "Attrition is 12% overall. Sales 18%, Eng 10%, Ops 8%.", "new_user": "what about engineers only?"},
        {"name": "Exclude interns / last 90d", "last_user": "show attrition by department", "last_assistant": "Attrition is 12% overall. Sales 18%, Eng 10%, Ops 8%.", "new_user": "last 90 days, exclude interns"},
    ],
    "Headcount": [
        {"name": "Q3 only", "last_user": "show headcount trends for 2023", "last_assistant": "Grew from 60 to 90 employees.", "new_user": "Q3 only"},
        {"name": "By location (incl contractors)", "last_user": "show headcount trends for 2023", "last_assistant": "Grew from 60 to 90 employees.", "new_user": "by location SF, include contractors"},
    ],
    "DEI": [
        {"name": "ICs slice", "last_user": "show DEI metrics for Q2 2024", "last_assistant": "Overall improved female leadership +3%.", "new_user": "just ICs"},
        {"name": "Senior IC vs last quarter", "last_user": "show DEI metrics for Q2 2024", "last_assistant": "Improved leadership +3%.", "new_user": "women in senior IC (L5+) vs last quarter"},
    ],
    "Recruiting": [
        {"name": "Include contractors", "last_user": "open reqs by org and seniority", "last_assistant": "14 total, Eng 8 (3 Sr+), Sales 4 (1 Sr+), Ops 2.", "new_user": "include contractors"},
        {"name": "SR roles H2 only", "last_user": "pipeline health for software engineer roles", "last_assistant": "Pass-through rate 28%, offer-accept 71%.", "new_user": "last 6 months, senior roles only"},
    ],
    "Perf & Comp": [
        {"name": "Compensation linkage", "last_user": "how do performance reviews work?", "last_assistant": "Annual in Q4 with calibration.", "new_user": "and compensation?"},
        {"name": "Engineers only", "last_user": "calibration guidelines", "last_assistant": "Use distribution bands; edge cases via VP approval.", "new_user": "for engineers only"},
    ],
    "Policies": [
        {"name": "Short PIP", "last_user": "PIP policy and template", "last_assistant": "Standard 60-day PIP with weekly checkpoints.", "new_user": "shorter 30-day version?"},
        {"name": "CA hourly PTO", "last_user": "PTO policy overview", "last_assistant": "Unlimited exempt; hourly accrue 1h/30h worked.", "new_user": "California hourly only"},
    ],
    "Edge Cases": [
        {"name": "Standalone (no rewrite)", "last_user": "", "last_assistant": "", "new_user": "show headcount by department and location for 2022–2024 with quarterly granularity"},
        {"name": "SQL guard (no rewrite)", "last_user": "show attrition by department", "last_assistant": "Sales 18%, Eng 10%, Ops 8%.", "new_user": "SELECT dept, COUNT(*) FROM employees WHERE terminated_at >= '2024-01-01';"},
    ]
}

def rewrite_debug(last_user, last_assistant, new_user):
    try:
        resp = requests.post(f"{API_URL}/v1/rewrite-debug", json={
            "last_user": last_user,
            "last_assistant": last_assistant,
            "new_user": new_user
        }, timeout=10)
        if resp.status_code == 200:
            return resp.json()
        else:
            return None
    except Exception:
        return None

def ask(query, k=8):
    try:
        resp = requests.post(f"{API_URL}/v1/ask", json={"query": query, "k": k}, timeout=15)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {"answer": "Error", "citations": []}
    except Exception:
        return {"answer": "Error", "citations": []}

def main():
    parser = argparse.ArgumentParser(description="Search Scenarios CLI")
    parser.add_argument("--group", type=str, default=None, help="Limit to scenario group")
    parser.add_argument("--ab", action="store_true", help="Run raw and rewritten calls")
    parser.add_argument("--k", type=int, default=8, help="Top-K")
    args = parser.parse_args()

    groups = [args.group] if args.group else SCENARIOS.keys()
    for group in groups:
        print(f"\n=== {group} ===")
        for scenario in SCENARIOS[group]:
            print(f"\nScenario: {scenario['name']}")
            print(f"Raw Input: {scenario['new_user']}")
            debug = rewrite_debug(scenario['last_user'], scenario['last_assistant'], scenario['new_user'])
            if debug:
                rewritten_query = debug.get("rewritten_query", scenario['new_user'])
                was_rewritten = debug.get("was_rewritten", False)
                print(f"Rewritten Query: {rewritten_query}")
                print(f"Was Rewritten: {was_rewritten}")
                print(f"Final Persona Prompt: {debug.get('persona_prompt','')}")
            else:
                rewritten_query = scenario['new_user']
                print("Rewrite debug not available, running raw only.")
            if args.ab:
                raw_result = ask(scenario['new_user'], k=args.k)
                rewritten_result = ask(rewritten_query, k=args.k)
                print(f"Raw Answer: {raw_result.get('answer','')[:120]}")
                print(f"Raw Citations: {raw_result.get('citations',[])[:2]}")
                print(f"Rewritten Answer: {rewritten_result.get('answer','')[:120]}")
                print(f"Rewritten Citations: {rewritten_result.get('citations',[])[:2]}")
            else:
                result = ask(rewritten_query, k=args.k)
                print(f"Answer: {result.get('answer','')[:120]}")
                print(f"Citations: {result.get('citations',[])[:2]}")

if __name__ == "__main__":
    main()
