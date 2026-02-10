from sqlalchemy.orm import Session
from src.user.models import User
from src.user.auth import verify_password


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

def create(db: Session, *,obj_in: dict):
    user=User(**obj_in)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user