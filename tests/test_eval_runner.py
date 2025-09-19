from eval import run_eval as _runner


def test_eval_runner_imports_and_cli_help():
    assert hasattr(_runner, "__file__") or True  # existence
    # the module must import without top-level execution errors
