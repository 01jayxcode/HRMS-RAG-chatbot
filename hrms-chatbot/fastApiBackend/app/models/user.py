from pydantic import BaseModel
from datetime import datetime
from typing import List

class Message(BaseModel):
    message: str
    timestamp: datetime

class User(BaseModel):
    id: int
    name: str
    messages: List[Message] = []