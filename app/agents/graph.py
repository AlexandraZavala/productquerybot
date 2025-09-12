from langgraph.graph import StateGraph, END 
from app.agents.responder import AgentResponder
from app.agents.retriever import AgentRetriever
from app.schema import StateMultiAgent 
from app.rag.store import VectorStore 


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


