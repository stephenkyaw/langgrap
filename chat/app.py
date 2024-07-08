from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages


# Defined the state with message string
class State(TypedDict):
    messages : Annotated[list,add_messages]


graph_builder = StateGraph(State)


# load llm model
from langchain_openai import ChatOpenAI


llm = ChatOpenAI(model="gpt-4-turbo")

def chatbot(state: State):
    return { "messages":[llm.invoke(state["messages"])] }

graph_builder.add_node("chatbot",chatbot)

graph_builder.add_edge(START,"chatbot")

graph_builder.add_edge("chatbot",END)


graph = graph_builder.compile()

while True:
    user_input = input("User: ")
    if user_input.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break
    for event in graph.stream({"messages": ("user", user_input)}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)
            print("------------------------------------------")