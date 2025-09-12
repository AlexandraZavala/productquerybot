
from langchain.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.docstore.document import Document
from typing import Iterable
import os
from dotenv import load_dotenv

load_dotenv()

model_name = str(os.getenv("EMBEDDING_MODEL_NAME"))


class VectorStore:
    def __init__(self, persist_directory: str, embedding_model_name: str = model_name):
        self.embedding_model = HuggingFaceEmbeddings(model_name=embedding_model_name)
        self.vector_store = Chroma(persist_directory=persist_directory, embedding_function=self.embedding_model)

    def add_documents(self, documents: Iterable[Document]):
        self.vector_store.add_documents(documents)
        self.vector_store.persist()

    def similarity_search(self, query: str, k: int) -> list[Document]:
        return self.vector_store.similarity_search(query, k=k)

    def has_content(self) -> bool:
       
        try:
            collection = self.vector_store._collection
            return collection.count() > 0
        except Exception:
            return False
