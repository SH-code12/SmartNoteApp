from sqlalchemy.orm import Session
from . import models


def create_note(db: Session, content: str, summary: str | None = None, tags: str | None = None):
    note = models.Note(content=content, summary=summary, tags=tags)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note

def get_notes(db: Session):
    return db.query(models.Note).all()

def delete_note(db: Session, note_id: int):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if note:
        db.delete(note)
        db.commit()
        return note
    return None

