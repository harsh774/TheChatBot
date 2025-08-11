# graph_builder.py
from langgraph.graph import StateGraph
from state_schema import State
from chatbot_node import chatbot

# Create and configure the state graph
graph_builder = StateGraph(State)

# Add the chatbot node
graph_builder.add_node("chatbot", chatbot)

# Set entry and exit points
graph_builder.set_entry_point("chatbot")
graph_builder.set_finish_point("chatbot")

# Compile the graph
chat_graph = graph_builder.compile()
