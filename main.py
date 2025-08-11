import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from pydantic import SecretStr
from graph_builder import chat_graph
from state_schema import State 

load_dotenv() 
print("DEBUG: OPENAI_API_KEY =", os.getenv("OPENAI_API_KEY"))


api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment.")

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7, api_key=SecretStr(api_key))

# Initial message
initial_state: State = {
    "messages": [HumanMessage(content="Hello! Can you explain LLM's?")]
}

# Run the graph
final_state = chat_graph.invoke(initial_state)

# Print results
for msg in final_state["messages"]:
    print(f"{msg.type}: {msg.content}")
