from pydantic import BaseModel, Field
from typing import Optional

class ChatRequest(BaseModel):
    conversation_id: str = Field(min_length=1)
    message: str = Field(min_length=1)

class ChatResponse(BaseModel):
    conversation_id: str
    response: str
    sources: list[str]

class Message(BaseModel):
    role: str
    content: str
    timestamp: str
