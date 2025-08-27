from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    summary = Column(String, nullable=True)
    tags = Column(String, nullable=True)
