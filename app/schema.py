from pydantic import BaseMode, Field

class QueryRequest(BaseModel):
    user_id: str = Field(..., description="The ID of the user making the request")
    query: str = Field(..., description="The user's query string")

class QueryResponse(BaseModel):
    response: str = Field(..., description="The response to the user's query")
