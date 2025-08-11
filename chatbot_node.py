# chatbot_node.py
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from state_schema import State

# Load environment variables
load_dotenv()

# Debug: print to ensure the key is being picked up
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError("❌ OPENAI_API_KEY not found. Please check your .env file and environment setup.")
else:
    print("✅ API Key loaded successfully.")

# Create the LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
# ✅ Do NOT pass `api_key=...` manually unless you're using SecretStr explicitly
# LangChain will auto-read from the env

def chatbot(state: State) -> State:
    messages = state["messages"]
    response = llm.invoke(messages)
    return {"messages": messages + [response]}
