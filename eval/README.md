
# RAG Service Evaluation Harness

This harness objectively measures:
- **Coverage**: % of required keywords (`must_have`) found in each answer
- **Citations**: Number of citations returned per answer
- **Latency**: API response time in milliseconds

## How to Run
- `make eval.sample` — Run on first 5 cases for a quick check
- `make eval.save` — Run full eval and save results to `eval/results/<timestamp>/`

## Acceptance Criteria
- A case passes if:
	- Coverage ≥ 80% of `must_have` keywords (case-insensitive, contains)
	- Citations ≥ `min_citations` (default 2)
- Overall acceptance: ≥80% cases pass AND ≥90% of answers have ≥2 citations

## Adding New Cases
- Edit `cases.csv` and add rows with:
	- `id`: unique string or number
	- `question`: the query to test
	- `must_have`: pipe-separated list of required tokens (e.g. `policy|duration|leave`)
	- `min_citations`: minimum citations required (default 2)
	- `k`: top-k passages to retrieve (default 8)
- `must_have` tokens are checked for simple containment in the answer (not exact match)

## Suggested Target
- Expand to 30+ cases covering diverse HR domains (benefits, compliance, payroll, onboarding, policies, etc.) for robust evaluation.
