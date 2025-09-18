
from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    DATA_RAW_DIR: Path = Path("data/raw")
    DATA_CLEAN_DIR: Path = Path("data/clean")

    # Allow list of directories from which we will serve files
    @property
    def FILE_SERVE_ROOTS(self) -> list[Path]:
        return [self.DATA_RAW_DIR.resolve(), self.DATA_CLEAN_DIR.resolve()]

settings = Settings()
