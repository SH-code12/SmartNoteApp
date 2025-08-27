from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Note-Taking App")
# For Gemini
router = APIRouter()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

@router.post("/summarize")
async def summarize(note: dict):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(
        f"Summarize and suggest tags for this note: {note['content']}"
    )
    return {"summary": response.text}

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
