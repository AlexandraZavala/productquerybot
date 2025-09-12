from pydantic import BaseModel, Field
from typing import TypedDict, List

class QueryInput(BaseModel):
    user_id: str = Field(..., description="The ID of the user making the request")
    query: str = Field(..., description="The user's query string")

class StateMultiAgent(TypedDict):
    user_id: str
    query: str
    docs: List[str]
    answer: str