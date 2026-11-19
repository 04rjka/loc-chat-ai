from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BACKEND_ROOT = Path(__file__).resolve().parents[1]
STORAGE_DIR = BACKEND_ROOT / "storage"

# Create storage directories
(STORAGE_DIR / "chroma").mkdir(parents=True, exist_ok=True)
(STORAGE_DIR / "uploads").mkdir(parents=True, exist_ok=True)

class Settings(BaseSettings):

    # Models
    ollama_base_url: str = "http://127.0.0.1:11434"
    embedding_model: str = "nomic-embed-text"
    llm_model: str = "gemma4:e2b"

    # Storage
    chroma_path: str = str(STORAGE_DIR / "chroma")
    upload_path: str = str(STORAGE_DIR / "uploads")
    database_url: str = f"sqlite:///{STORAGE_DIR / 'app.db'}"

    # Server
    cors_origins: str = "http://localhost:3000,http://127.0.0.1:3000"

    @property
    def cors_origins_list(self) -> list[str]:
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]

    model_config = SettingsConfigDict(
        env_file= BACKEND_ROOT / ".env",
        extra="ignore",
    )

settings = Settings()