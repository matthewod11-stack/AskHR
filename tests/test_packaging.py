def test_import_app_config():
    import importlib

    mod = importlib.import_module("app.config")
    assert hasattr(mod, "BaseSettings")


def test_pydantic_settings_available():
    import importlib

    ps = importlib.import_module("pydantic_settings")
    assert hasattr(ps, "BaseSettings")
