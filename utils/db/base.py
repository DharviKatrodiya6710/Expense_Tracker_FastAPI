import datetime, uuid
from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.orm import as_declarative, declared_attr

def str_uuid():
    return str(uuid.uuid4())

@as_declarative()
class ModelBase:
    id = Column(String, primary_key=True, default=str_uuid)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    is_deleted = Column(Boolean, default=False)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
