from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.user.models import User
from src.user.models import hash_password, verify_password, create_access_token

def register_user(db: Session, user):
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(400, "User already exists")

    new_user = User(
        username=user.username,
        password=hash_password(user.password),
        is_admin=user.is_admin   
    ) 
    db.add(new_user)
    db.commit()
    return {"message": "User registered successfully"}


def login_user(db: Session, username: str, password: str):
    db_user = db.query(User).filter(User.username == username).first()

    if not db_user or not verify_password(password, db_user.password):
        raise HTTPException(401, "Invalid credentials")

    token = create_access_token({
        "user_id": db_user.id,
        "is_admin": db_user.is_admin
    })

    return token

#notes

# remember dharvi

#401 - unauthorized, token invalid
#403 - forbidden - that means already create login but you not have permission
#404 - not found
#500 - server side error
#200 - request OK
#201 - create
#400 - bad request - wrong data 

# filter() - to data get in database

#first() - this function to give first matching data in record