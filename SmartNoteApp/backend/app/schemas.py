# schemas.py
from pydantic import BaseModel
from typing import List, Optional

class NoteCreate(BaseModel):
    content: str

class NoteOut(BaseModel):
    id: int
    content: str
    summary: Optional[str]
    tags: Optional[List[str]]
