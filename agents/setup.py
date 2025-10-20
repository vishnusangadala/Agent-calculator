from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain.memory import ConversationBufferMemory
from langchain import hub
from agents.tools import TOOLS

def create_agent_executor(llm) -> AgentExecutor:

    #  Short-term memory across turns (resets when the process restarts)
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
    )

    prompt = hub.pull("hwchase17/react-chat")

    agent = create_react_agent(
        llm=llm,
        tools=TOOLS,
        prompt=prompt,
    )

    return AgentExecutor(
        agent=agent,
        tools=TOOLS,
        memory=memory,
        verbose=True,
        handle_parsing_errors=True,
    )
