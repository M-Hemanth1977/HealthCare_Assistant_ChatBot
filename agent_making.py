import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun,WikipediaQueryRun,ArxivQueryRun
from langchain_community.utilities import WikipediaAPIWrapper,ArxivAPIWrapper,DuckDuckGoSearchAPIWrapper
from langchain.agents import initialize_agent,AgentType

load_dotenv(dotenv_path=r"D:\Lang_chain\.env")


llm=ChatGroq(model="llama3-8b-8192",api_key=os.getenv("groq_api_key"))

wiki_wrapper=WikipediaAPIWrapper(top_k_results=1)
arxiv_wrapper=ArxivAPIWrapper(top_k_results=1)
duck_wrapper=DuckDuckGoSearchAPIWrapper(max_results=1)

wiki=WikipediaQueryRun(api_wrapper=wiki_wrapper)
arxiv=ArxivQueryRun(api_wrapper=arxiv_wrapper)
duck=DuckDuckGoSearchRun(api_wrapper=duck_wrapper)

tools=[wiki,arxiv]

agent=initialize_agent(tools=tools,llm=llm,agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,verbose=False,handle_parsing_errors=True)

# print(agent)