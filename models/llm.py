import os
from langchain_openai import ChatOpenAI
from config import app_config

def init_llm(api_key: str) -> ChatOpenAI:
    # Disable LangSmith tracing warnings
    os.environ["LANGCHAIN_TRACING_V2"] = "false"

    return ChatOpenAI(
        model=app_config.MODEL_NAME,
        temperature=app_config.TEMPERATURE,
        max_tokens=app_config.MAX_TOKENS,
        timeout=app_config.TIMEOUT,
        api_key=api_key,
    )
