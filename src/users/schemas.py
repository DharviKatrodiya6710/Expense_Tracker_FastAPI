from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    age: int = Field(..., ge=3, le=100)

class LoginRequest(BaseModel):
    username: str
    password: str
    is_Admin:bool = False


#notes

#pydantic - data validate or note
#basemodel - that is base class of pydantic

