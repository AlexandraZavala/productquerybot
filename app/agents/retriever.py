from langchain.docstore.document import Document
from app.rag.store import VectorStore
from app.schema import StateMultiAgent
import os
from dotenv import load_dotenv

load_dotenv()

k = int(os.getenv("TOP-K"))  # Número de documentos a recuperar

class AgentRetriever:
    """Agent that retrieves relevant documents based on a user query."""
    def __init__(self, vector_store: VectorStore):
        self.vector_store = vector_store

    def __call__(self, state: StateMultiAgent) -> StateMultiAgent:
        state['docs'] = self.vector_store.similarity_search(state['query'], k=k)
        return state