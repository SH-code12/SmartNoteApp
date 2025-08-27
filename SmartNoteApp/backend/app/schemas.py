from pydantic import BaseModel
from typing import List, Optional


class NoteCreate(BaseModel):
    content: str
    summary: str | None = None
    tags: str | None = None

class NoteOut(BaseModel):
    id: int
    content: str
    summary: str | None = None
    tags: str | None = None

    class Config:
        orm_mode = True


