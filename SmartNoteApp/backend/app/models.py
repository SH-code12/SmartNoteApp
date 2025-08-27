# models.py
from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    summary = Column(Text)
    tags = Column(String)  # store comma-separated tags for simplicity
