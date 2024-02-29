from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.callbacks import StreamingStdOutCallbackHandler

from .prompt_template import scribe_prompt
from .tools import (
    read_all_todos,
    clear_all_todos,
    delete_todo,
    add_todo,
    get_curr_time,
    update_todo
)


class Scribe:

    def __init__(self):
        # self.collection_name = collection_name
        self.llm = ChatOpenAI(
            model='gpt-3.5-turbo',
            temperature=0.1,
            callbacks=[StreamingStdOutCallbackHandler()]
        )
        self.prompt = scribe_prompt
        self.tools = [
            read_all_todos,
            clear_all_todos,
            add_todo,
            get_curr_time,
            delete_todo,
            update_todo
        ]

        self.agent = create_openai_functions_agent(self.llm, self.tools, self.prompt)
        self.agent_executor = AgentExecutor(
            agent=self.agent,
            tools=self.tools,
            verbose=True
        )

    async def ask(self, prompt: str, collection_name: str):
        # ainvoke allows usage of async code (I guess this applies for tools)
        return await self.agent_executor.ainvoke(
            input={'collection_name': collection_name, 'input': prompt}
        )
