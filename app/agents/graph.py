from langgraph.graph import StateGraph, END 
from .responder import AgentResponder
from .retriever import AgentRetriever
from schema import StateMultiAgent 
from rag.store import VectorStore 


class MultiAgentGraph(StateGraph[StateMultiAgent]):
    def __init__(self):
        self.vector_store = VectorStore(persist_directory="vector_store")
        self.retriever = AgentRetriever(self.vector_store)
        self.responder = AgentResponder()
        self.graph = StateGraph(StateMultiAgent)
        self.graph.add_node("retrieve", self.retriever)
        self.graph.set_entry_point("retrieve")
        self.graph.add_node("respond", self.responder)
        self.graph.add_edge("retrieve", "respond")
        self.graph.add_edge("respond", END)
        self.app = self.graph.compile()
    
    def run (self, state: StateMultiAgent) -> StateMultiAgent:
        return self.app.invoke(state)


