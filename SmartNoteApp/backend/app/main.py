# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Note-Taking App")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/notes", response_model=schemas.NoteOut)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    created_note = crud.create_note(db, content=note.content)
    return created_note

@app.get("/api/notes", response_model=list[schemas.NoteOut])
def read_notes(db: Session = Depends(get_db)):
    return crud.get_notes(db)

@app.delete("/api/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = crud.delete_note(db, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"msg": "Deleted successfully"}

@app.post("/api/notes/summarize")
def summarize_note(note: schemas.NoteCreate):
    # Call Gemini Studio API
    import requests
    GEMINI_API_KEY = "YOUR_KEY"
    response = requests.post(
        "https://api.gemini.example/summarize",
        json={"text": note.content},
        headers={"Authorization": f"Bearer {GEMINI_API_KEY}"}
    )
    summary_data = response.json()
    return summary_data
