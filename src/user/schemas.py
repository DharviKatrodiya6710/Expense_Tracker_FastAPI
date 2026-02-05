from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    is_admin:bool = False

class LoginRequest(BaseModel):
    username: str
    password: str
    is_Admin:bool = False


#notes

#pydantic - data validate or note
#basemodel - that is base class of pydantic

