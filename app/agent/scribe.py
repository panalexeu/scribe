from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openapi_agent


class Scribe:

    def __init__(self):
        # self.collection_name = collection_name
        self.llm = ChatOpenAI(
            model='gpt-3.5-turbo',
        )
        self.prompt = None
        self.tools = None

        self.agent = (self.llm, self.tools, self.prompt)
        self.agent_executor = AgentExecutor(
            agent=self.agent,
            tools=self.tools
        )

    async def ask(self, prompt: str, collection_name: str):
        return self.agent_executor.invoke(
            input={'collection_name': collection_name, 'input': prompt}
        )
