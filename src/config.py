from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    DATABASE_URL: str
    CHUNK_SIZE: int = 10000
    LOG_FILE: str = "logs/errors.log"
    DATA_DIR: Path = Path("data")

    @property
    def CSV_FILE_PATH(self) -> Path:
        csv_files = list(self.DATA_DIR.glob("*.csv"))

        if not csv_files:
            raise FileNotFoundError(f"No CSV files found in {self.DATA_DIR}")
        
        return max(csv_files, key=lambda f: f.stat().st_mtime)  # Pick the latest modified file

    class Config:
        env_file = ".env"


settings = Settings()
