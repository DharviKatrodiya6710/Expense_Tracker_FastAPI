from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from utils.db.session import get_db
from src.notes.schemas import Notecreate, Noteupdate, Noteout
from src.notes import crud
from src.user.auth import get_current_user

api_router = APIRouter(prefix="/notes", tags=["Notes"])


@api_router.post("/add", response_model=Noteout)
def add_note(
    note: Notecreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return crud.create_note(db, note, user_id=user.id)

@api_router.put("/update")
def update_note(
    note_id: int,
    note: Noteupdate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    updated = crud.update_note(db, note_id, note, user_id=user.id)
    if not updated:
        raise HTTPException(status_code=404, detail="Note not found")
    return updated


@api_router.delete("/delete")
def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    deleted = crud.delete_note(db, note_id, user_id=user.id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note deleted"}

@api_router.get("/list")
def list_notes(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return crud.get_notes(db, user_id=user.id)

