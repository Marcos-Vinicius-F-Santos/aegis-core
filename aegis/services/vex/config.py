from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
	OLLAMA_URL: str = "http://localhost:11434/api/generate"
	DEFAULT_MODEL: str = "llama3.2:3b"
	REQUEST_TIMEOUT: int = 120

settings = Settings()
