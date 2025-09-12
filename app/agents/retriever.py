from langchain.docstore.document import Document
from rag.store import VectorStore
from schema import StateMultiAgent

class AgentRetriever:
    def __init__(self, vector_store: VectorStore):
        self.vector_store = vector_store

    def __call__(self, state: StateMultiAgent) -> StateMultiAgent:
        state['docs'] = self.vector_store.similarity_search(state['query'], k=3, )
        print(f"Documentos recuperados: {len(state['docs'])}")
        print(f"Contenido del primer documento: {state['docs'][0].page_content if state['docs'] else 'No hay documentos'}")
        return state