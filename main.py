# main.py
from pathlib import Path
from dotenv import dotenv_values
from langchain_openai import ChatOpenAI
from langchain.agents.agent import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain import hub
import os

# Import your tools (make sure tools.py is in the same folder)
from tools import TOOLS

# --- Load API key directly from .env ---
cfg = dotenv_values(Path(__file__).parent / ".env")
api_key = cfg.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY missing in .env")

# --- Optional: disable LangSmith tracing warning ---
os.environ["LANGCHAIN_TRACING_V2"] = "false"

# --- Initialize LLM ---
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.1,
    max_tokens=500,
    timeout=30,
    api_key=api_key
)

# --- Build ReAct Agent ---
prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm=llm, tools=TOOLS, prompt=prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=TOOLS,
    verbose=True,
    handle_parsing_errors=True
)

# --- Interactive session ---
if __name__ == "__main__":
    print("\n Agent ready! Type a query")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        query = input("👉 Your query: ").strip()
        if query.lower() in {"exit", "quit", "q"}:
            print("👋 Exiting... Goodbye!")
            break

        try:
            result = agent_executor.invoke({"input": query})
            print("\n--- Agent Output ---")
            print(result.get("output", result), "\n")
        except Exception as e:
            print(f"Error: {e}\n")
