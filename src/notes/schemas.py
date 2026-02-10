from pydantic import BaseModel

class  Notecreate(BaseModel):
    title : str
    description: str

class Noteupdate(BaseModel):
    title: str
    description: str

class Noteout(BaseModel):
    id: int
    title: str
    description : str

    class ConfigDict:
        from_attributes = True