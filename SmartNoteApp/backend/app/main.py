from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import SessionLocal, engine
import requests
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Smart Note-Taking App")


class SummarizeRequest(BaseModel):
    content: str

class SummarizeResponse(BaseModel):
    summary: str
    tags: list[str]

API_KEY = "AIzaSyCfN9eaH4HT_PlaSminF3m0anqySNUEXzw"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

# Create tables
models.Base.metadata.create_all(bind=engine)

# --- Add CORS configuration here ---
origins = [
    "http://localhost:3000",       # React dev server
    "http://192.168.1.10:3000",    # Your LAN IP if accessing from other devices
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,         # allow these origins
    allow_credentials=True,
    allow_methods=["*"],           # allow all HTTP methods
    allow_headers=["*"],           # allow all headers
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/createnotes", response_model=schemas.NoteOut)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    created_note = crud.create_note(
        db,
        content=note.content,
        summary=note.summary,
        tags=note.tags
    )
    return created_note


@app.get("/api/getnotes", response_model=list[schemas.NoteOut])
def read_notes(db: Session = Depends(get_db)):
    return crud.get_notes(db)

@app.delete("/api/deletenotes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = crud.delete_note(db, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"msg": "Deleted successfully"}

#@app.post("/api/summarize", response_model=SummarizeResponse)
#def summarize_note_api(request: SummarizeRequest):
    # Replace the next line with your actual summarization logic
 #   summary_text = f"Summary of: {request.content[:50]}..."  
 #   return {"summary": summary_text}


@app.post("/api/summarize", response_model=SummarizeResponse)
def summarize_note_api(request: SummarizeRequest):
    payload = {
        "contents": [{"parts": [{"text": request.content}]}]
    }

    response = requests.post(API_URL, json=payload)
    data = response.json()

    summary = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
    
    return {
        "summary": summary,
        "tags": []  # you can implement your own tag extraction logic
    }

@app.put("/api/updatenotes/{note_id}", response_model=schemas.NoteOut)
def update_note(note_id: int, note: schemas.NoteUpdate, db: Session = Depends(get_db)):
    return crud.update_note(db, note_id, note)

@app.get("/api/searchnotes")
def search_notes(q: str, db: Session = Depends(get_db)):
    return crud.search_notes(db, q)

