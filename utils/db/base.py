import datetime
from sqlalchemy import Boolean, Column, DateTime, Integer
from sqlalchemy.orm import declarative_base, declared_attr

Base = declarative_base()

class ModelBase(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)

    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )

    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        nullable=False,
    )

    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)

    is_deleted = Column(Boolean, default=False, nullable=False)

    @declared_attr
    def __tablename__(cls):
        name = cls.__name__
        result = ""
        prev_upper = False

        for i, ch in enumerate(name):
            if ch.isupper() and (i == 0 or not prev_upper):
                result += "_" + ch.lower()
            else:
                result += ch.lower()
            prev_upper = ch.isupper()

        return result.lstrip("_")
