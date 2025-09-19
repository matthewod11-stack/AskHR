from eval.utils import load_cases


def test_eval_cases_csv_loads_and_has_headers():
    rows = load_cases("eval/cases.csv")
    assert len(rows) >= 5
    r0 = rows[0]
    assert hasattr(r0, "id")
    assert hasattr(r0, "query")
    assert hasattr(r0, "expect_grounded")
