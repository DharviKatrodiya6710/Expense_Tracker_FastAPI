from datetime import datetime, timedelta
from typing import Optional
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
security = HTTPBearer()


from fastapi import Depends, HTTPException, status, Header
from jose import jwt, JWTError
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from utils.db.session import get_db
from src.config import Config
from src.user import crud

from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(
    data: dict,
    expires_delta: Optional[timedelta] = None
) -> str:
    to_encode=data.copy()

    if "user_id" in to_encode:
        to_encode["sub"] = str(to_encode.pop("user_id"))

    expire = datetime.utcnow() + (
        expires_delta
        if expires_delta
        else timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
    )   
    to_encode.update({
        "exp" :expire,
        "type": "access"
    })
    return jwt.encode(
        to_encode,
        Config.SECRET_KEY,
        algorithm=Config.ALGORITHM
    ) 

def get_current_user(
    creds: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = creds.credentials
    payload = jwt.decode(
        token,
        Config.SECRET_KEY,
        algorithms=[Config.ALGORITHM]
    )
    user_id = int(payload["sub"])
    return crud.get_user_by_id(db, user_id)