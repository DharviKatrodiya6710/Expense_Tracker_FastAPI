from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from utils.database import SessionLocal
from config import Config

security = HTTPBearer()

def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    payload = jwt.decode(token, Config.SECRET_KEY, algorithms=[Config.ALGORITHM])

    user_id = payload.get("sub")
    role = payload.get("role")

    if user_id is None or role is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )
    return {
            "user_id": int(user_id),
            "role": role
        }


def admin_only(
    current_user = Depends(get_current_user)
) -> dict:
    if current_user["role"] != "ADMIN":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return current_user
