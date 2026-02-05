from typing import Optional
from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class BaseCreateSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class BaseResponseSchema(BaseSchema):
    id: int
    is_deleted: Optional[bool] = False
    created_by: Optional[str] = None
    updated_by: Optional[str] = None
