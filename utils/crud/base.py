from typing import Any, Dict, Type, TypeVar, Generic
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import false
from utils.db.base import ModelBase

ModelType = TypeVar("ModelType", bound=ModelBase)

class CRUDBase(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, id: Any):
        return db.query(self.model).filter(
            self.model.id == id,
            self.model.is_deleted == false()
        ).first()

    def create(self, db: Session, *, obj_in: Dict[str, Any]):
        db_obj = self.model(**obj_in)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
