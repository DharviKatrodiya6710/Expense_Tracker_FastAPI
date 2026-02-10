from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from utils.db.session import get_db
from src.user import crud
from src.user.schemas import UserCreate, UserLogin, access_token
from src.user.auth import ( hash_password, verify_password, create_access_token, get_current_user)


api_router = APIRouter()



@api_router.post("/register", status_code=201)
def register(
    payload: UserCreate,
    db: Session = Depends(get_db)
):
    existing = crud.get_user_by_email(db, payload.email)
    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    hashed = hash_password(payload.password)

    return crud.create(
        db,
        obj_in={
            "email": payload.email,
            "hashed_password": hashed,
            "role": payload.role,
            "firstname":payload.firstname,
            "lastname":payload.lastname,
            "phone_number_country_code":payload.phone_number_country_code,
            "phone_number":payload.phone_number
        }
    )

@api_router.post("/login", response_model= access_token)
def login(
    payload: UserLogin,
    db: Session = Depends(get_db)
):
    user = crud.get_user_by_email(db, payload.email)

    if not user or not verify_password(
        payload.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    access_token = create_access_token(
        {"user_id": user.id, "role": user.role}
    )
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
@api_router.get("/me")
def me(current_user = Depends(get_current_user)):
    return {"id": current_user.id,
            "email":current_user.email
            }
