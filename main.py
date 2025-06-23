import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit as st
from transformers import AutoTokenizer,AutoModelForCausalLM
from peft import PeftModel
import torch
from agent_making import agent
from llm import template,parser,llm
from langchain_core.runnables import RunnableParallel
from operator import itemgetter

os.environ["LANGSMITH_TRACING"]="true"
os.environ["LANGSMITH_API_KEY"]=os.getenv("langsmith_api_key")
os.environ["LANGSMITH_PROJECT"]="HealthCare_Assistant_Chatbot"

load_dotenv(dotenv_path=r"D:\Lang_chain\.env")

st.title("HEALTH CARE ASSISTANT CHATBOT")

os.environ["HF_TOKEN"]=os.getenv("hf_api_key")

base_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
base_model=AutoModelForCausalLM.from_pretrained(base_id)
pt_model=PeftModel.from_pretrained(base_model,"./llama3-lora-qa")
tokenizer=AutoTokenizer.from_pretrained("./llama3-lora-qa")

if "messages" not in st.session_state:
    st.session_state["messages"]=[{
        "role":"ai",
        "content":"Hi, I am a AI assiatnt how can i help you"
    }]

for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

if user_input:=st.chat_input(placeholder="Enter your query?"):

    st.session_state["messages"].append(
        {
            "role":"human",
            "content":user_input
        }
    )

    st.chat_message("human").write(user_input)

    pt_model.eval()

    with torch.no_grad():

        input_tokens=tokenizer(user_input,return_tensors="pt").to("cpu")

        output = pt_model.generate(
            input_ids=input_tokens["input_ids"],
            attention_mask=input_tokens["attention_mask"],
            max_new_tokens=200,
            temperature=0.7,
            do_sample=True,
            eos_token_id=tokenizer.eos_token_id
        )

    fine_tuned_response=tokenizer.decode(output[0], skip_special_tokens=True,clean_up_tokenization_spaces=True)

    llm_response=agent.invoke({"input":user_input})
    general_llm_response=llm_response["output"]

    chain=RunnableParallel({"input":itemgetter("input"),
                            "history":itemgetter("history"),
                            "fine_tuned_output":itemgetter("fine_tuned_output"),
                            "agent_output":itemgetter("agent_output")})|template|llm|parser

    res=chain.invoke({"input":user_input,
                      "history":st.session_state["messages"],
                      "fine_tuned_output":[{"role":"ai","content":fine_tuned_response}],
                      "agent_output":[{"role":"ai","content":general_llm_response}]})
    
    st.chat_message("ai").write(res)

    st.session_state["messages"].append({
        "role":"ai",
        "content":res
    })

