import logging
from pathlib import Path

from pydantic import PostgresDsn, computed_field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn
    CHUNK_SIZE: int = 10000
    LOG_FILE: str = "logs/errors.log"
    DATA_DIR: Path = Path("data")

    @computed_field
    @property
    def ASYNC_DATABASE_URL(self) -> str:
        """Convert DATABASE_URL to async format for SQLAlchemy"""
        return str(self.DATABASE_URL).replace("postgresql://", "postgresql+asyncpg://")

    @property
    def CSV_FILE_PATH(self) -> Path:
        csv_files = list(self.DATA_DIR.glob("*.csv"))

        if not csv_files:
            raise FileNotFoundError(f"No CSV files found in {self.DATA_DIR}")

        return max(
            csv_files, key=lambda f: f.stat().st_mtime
        )  # Pick the latest modified file

    class Config:
        env_file = ".env"


settings = Settings()
logging.basicConfig(
    filename=settings.LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
