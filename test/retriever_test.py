import pytest
import sys
import os
from langchain.docstore.document import Document
from app.rag.store import VectorStore
from app.agents.retriever import AgentRetriever


def load_products_from_txt(path="document_corpus.txt"):
    docs = []
    with open(path, encoding="utf-8") as f:
        content = f.read()
    for i, block in enumerate(content.split("=== PRODUCTO ===")):
        block = block.strip()
        if not block:
            continue
        docs.append(Document(
            page_content=block,
            metadata={"source": f"producto_{i+1}.txt"}
        ))
    return docs

@pytest.fixture(scope="session")
def retriever(tmp_path_factory):
    # Vector store temporal
    tmpdir = tmp_path_factory.mktemp("chroma-test")
    vs = VectorStore(persist_directory=str(tmpdir))

    docs = load_products_from_txt("document_corpus.txt")
    vs.add_documents(docs)

    return AgentRetriever(vs)

def test_retriever_finds_laptop(retriever):
    state = {"user_id": "u1", "query": "portátil con CUDA y pantalla OLED"}
    out = retriever(state)
    assert "docs" in out and len(out["docs"]) > 0
    # Verificamos que alguno de los docs recuperados contiene "ZenBook"
    assert any("ZenBook" in d.page_content for d in out["docs"])

def test_retriever_returns_something_for_phone(retriever):
    state = {"user_id": "u1", "query": "móvil compacto con buena cámara"}
    out = retriever(state)
    assert len(out["docs"]) > 0
    assert any("Nova X" in d.page_content for d in out["docs"])
