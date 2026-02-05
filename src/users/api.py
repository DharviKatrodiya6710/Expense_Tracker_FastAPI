import logging
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from utils.db.session import get_db
from src.user.schemas import UserCreate,LoginRequest
from src.user.crud import register_user, login_user
from src.user.models import get_current_user

logger = logging.getLogger(__name__)

api_router = APIRouter(prefix="/user", tags=["User"])

@api_router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user)

@api_router.post("/login")
def login(
    user:LoginRequest,db:get_db):
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)

    token = login_user(db, form_data.username, form_data.password)
    return {"access_token": token, "token_type": "bearer"}

@api_router.get("/me")
def me():
    user_id=1
    user = get_user_by_id(user_id)
    return user



