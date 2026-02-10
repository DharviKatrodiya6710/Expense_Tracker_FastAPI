from sqlalchemy.orm import Session
from src.notes.models import Note

def create_note(db: Session,note,user_id:int):
    new_note = Note(
        title=note.title,
        description=note.description,
        user_id=user_id
    )
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

def get_notes(db: Session,user_id:int):
    return db.query(Note).filter(Note.user_id == user_id).all()

def update_note(db: Session,note_id: int,note,user_id:int):
    db_note=db.query(Note).filter(
        Note.id == note_id,
        Note.user_id == user_id
    ).first()

    if not db_note:
        return None
    
    db_note.title=note.title
    db_note.description=note.description
    db.commit()
    db.refresh(db_note)
    return db_note

def delete_note(db: Session,note_id:int,user_id:int):
    db_note = db.query(Note).filter(
        Note.id == note_id,
        Note.user_id == user_id
    ).first()

    if not db_note:
        return None
    
    db.delete(db_note)
    db.commit()
    return True