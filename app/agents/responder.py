from langchain_openai import ChatOpenAI
from schema import StateMultiAgent

SYSTEM_PROMPT = """Eres un asistente útil que ayuda a responder consultas de usuarios con respecto a productos.

Proporciona respuestas en español.
"""

class AgentResponder:
    def __init__(self, model_name: str = "gpt-3.5-turbo", temperature: float = 0.7):
        self.llm = ChatOpenAI(model_name=model_name, temperature=temperature)

    def __call__(self, state: StateMultiAgent) -> StateMultiAgent:
        context = "\n".join([doc.page_content for doc in state['docs']])
        prompt = f"{SYSTEM_PROMPT}\n\nContext:\n{context}\n\nUser Query: {state['query']}\n\nAnswer:"
        response = self.llm.predict(prompt)
        state['answer'] = response
        return state
