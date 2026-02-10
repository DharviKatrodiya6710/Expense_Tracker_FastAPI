import os
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

DATABASE_URL = "postgresql+psycopg2://postgres:dharvi@localhost:5432/tracker_system"


class Config:
    DB_USER = "postgres"
    DB_PASSWORD = "dharvi"
    DB_HOST = "localhost"
    DB_PORT = "5432"
    DB_NAME = "tracker_system"  

    SECRET_KEY = os.getenv("SECRET_KEY", "SUPER_SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60

    @classmethod
    def assemble_db_connection(cls) -> str:
        return (
            f"postgresql+psycopg2://{cls.DB_USER}:{cls.DB_PASSWORD}"
            f"@{cls.DB_HOST}:{cls.DB_PORT}/{cls.DB_NAME}"
        )

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)

def create_access_token(
    data: dict,
    expires_delta: timedelta | None = None
) -> str:
    to_encode = data.copy()

    
    if "user_id" in to_encode:
        to_encode["sub"] = str(to_encode.pop("user_id"))

    expire = datetime.utcnow() + (
        expires_delta
        if expires_delta
        else timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    to_encode.update({
        "exp": expire,
        "type": "access"
    })

    return jwt.encode(
        to_encode,
        Config.SECRET_KEY,
        algorithm=Config.ALGORITHM
    )

#notes dharvi

#timedelta=difference between two dates or times