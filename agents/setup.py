from langchain import hub
from langchain.agents.react.agent import create_react_agent
from langchain.agents import AgentExecutor
from agents.tools import TOOLS

def create_agent_executor(llm) -> AgentExecutor:
    # Load the default ReAct prompt template
    prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(
        llm=llm,
        tools=TOOLS,
        prompt=prompt,
    )

    return AgentExecutor(
        agent=agent,
        tools=TOOLS,
        verbose=True,
        handle_parsing_errors=True,
    )
