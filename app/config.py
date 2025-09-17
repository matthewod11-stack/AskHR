import os
from pathlib import Path

class Settings:
    """Configuration settings for the AskHR application."""
    
    def __init__(self):
        # Get the root directory (parent of app/)
        self.ROOT = Path(__file__).resolve().parents[1]
        
        # Data directories
        self.DATA_RAW_DIR = Path(os.getenv("DATA_RAW", str(self.ROOT / "data" / "raw")))
        self.DATA_CLEAN_DIR = Path(os.getenv("DATA_CLEAN", str(self.ROOT / "data" / "clean")))

# Global settings instance
settings = Settings()