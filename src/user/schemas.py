from pydantic import BaseModel,EmailStr, Field
from typing import Literal, Optional
from utils.schemas.base import BaseCreateSchema, BaseResponseSchema


class UserCreate(BaseCreateSchema):
    email: EmailStr
    password: str = Field(..., min_length=6)
    role: Literal["ADMIN", "USER"] = "USER"
    firstname:str | None = None
    lastname: str | None = None
    phone_number_country_code:str | None = None
    phone_number:str | None = None

class UserUpdate(BaseCreateSchema):
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: Optional[Literal["ADMIN", "USER"]] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseResponseSchema):
    email: EmailStr
    role: str

class access_token(BaseModel):
    access_token: str
    token_type: str = "bearer"






#notes

#pydantic - data validate or note
#basemodel - that is base class of pydantic

