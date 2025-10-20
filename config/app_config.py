from pathlib import Path
from dotenv import dotenv_values

# Centralized environment + configuration manager
def load_api_key() -> str:
    cfg = dotenv_values(Path(__file__).parents[1] / ".env")
    api_key = cfg.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY missing in .env")
    return api_key

# Optional: Add other global configs here
MODEL_NAME = "gpt-4o"
TEMPERATURE = 0.1
MAX_TOKENS = 500
TIMEOUT = 30
