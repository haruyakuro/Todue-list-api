from pydantic import BaseModel
from typing import Optional

class ItemCreate(BaseModel):
    name: str
    kind: str
    date: str
    score: int

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    kind: Optional[str] = None
    date: Optional[str] = None
    score: Optional[int] = None

class ItemResponse(BaseModel):
    id: int
    name: str
    kind: str
    date: str
    score: int

