import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

load_dotenv(dotenv_path=r"D:\Lang_chain\.env")

llm=ChatGroq(model="llama3-8b-8192",api_key=os.getenv("groq_api_key"))

template=ChatPromptTemplate.from_messages(
    [
        ("ai","""You are a healthcare AI assistant Expert. You are given two responses and history include everything and 
        Provide a response in a detailed and in simple way """),
        MessagesPlaceholder(variable_name="agent_output"),
        MessagesPlaceholder(variable_name="fine_tuned_output"),
        MessagesPlaceholder(variable_name="history"),
        ("user","{input}")
    ]
)

parser=StrOutputParser()

# print("Exceution done succesfully")


