from langchain.docstore.document import Document
from rag.store import VectorStore
from schema import StateMultiAgent

class AgentRetriever:
    """Agent that retrieves relevant documents based on a user query."""
    def __init__(self, vector_store: VectorStore):
        self.vector_store = vector_store

    def __call__(self, state: StateMultiAgent) -> StateMultiAgent:
        state['docs'] = self.vector_store.similarity_search(state['query'], k=3, )
        return state