from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import Iterable, List
from store import VectorStore


def index_documents(file_name: str = "document_corpus.txt", chunk_size: int = 300, chunk_overlap: int = 50) -> List[Document]:

    print("Indexing documents...")
    with open(file_name, "r") as f:
        text = f.read()
    print(f"Read {len(text)} characters from {file_name}")

    documents = [Document(page_content=text)]

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    split_docs = text_splitter.split_documents(documents)

    vector_store = VectorStore(persist_directory="vector_store", embedding_model_name="sentence-transformers/all-mpnet-base-v2")
    vector_store.add_documents(split_docs)

    vs = VectorStore("vector_store")
    if vs.has_content():
        print("El vector store tiene contenido.")
    else:
        print("El vector store está vacío.")

    return split_docs

if __name__ == "__main__":
    index_documents()