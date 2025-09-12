
from fastapi import FastAPI, Request
from pydantic import BaseModel
from agents.graph import MultiAgentGraph
from schema import StateMultiAgent, QueryInput
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.post("/query")
async def query_endpoint(data: QueryInput):
	# Validar input
	if not data.user_id or not data.query:
		return {"error": "user_id y query son requeridos"}
	state = StateMultiAgent(user_id=data.user_id, query=data.query, docs=[], answer="")
	mag = MultiAgentGraph()
	result = mag.run(state)
	return {"response": result.get("answer", result)}

if __name__ == "__main__":
	uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
