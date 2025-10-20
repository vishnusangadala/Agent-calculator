from config.app_config import load_api_key
from models.llm import init_llm
from agents.setup import create_agent_executor
from runtime.interactive import start_session

if __name__ == "__main__":
    api_key = load_api_key()
    llm = init_llm(api_key)
    agent_executor = create_agent_executor(llm)
    start_session(agent_executor)
