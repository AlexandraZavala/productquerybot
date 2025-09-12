from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import Iterable, List
from app.store import VectorStore
import os
from dotenv import load_dotenv

load_dotenv()

model_name = str(os.getenv("EMBEDDING_MODEL_NAME"))

def index_documents(file_name: str = "document_corpus.txt", chunk_size: int = 300, chunk_overlap: int = 50) -> List[Document]:
    """Index documents from a text file into the vector store."""
    with open(file_name, "r") as f:
        text = f.read()

    documents = [Document(page_content=text)]

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    split_docs = text_splitter.split_documents(documents)

    vector_store = VectorStore(persist_directory="vector_store", embedding_model_name=model_name)
    vector_store.add_documents(split_docs)

    vs = VectorStore("vector_store")

    return split_docs

if __name__ == "__main__":
    index_documents()