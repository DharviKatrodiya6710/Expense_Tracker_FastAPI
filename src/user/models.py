
from sqlalchemy import Column, String, Integer
from utils.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False)
    firstname = Column(String,nullable=True)
    lastname=Column(String,nullable=True)
    phone_number_country_code = Column(Integer,nullable=True)
    phone_number=Column(Integer,nullable=True)

def __repr__(self):
    return f"""
        User INFO:
        ID:{self.id}
        EMAIL:{self.email}
        PASSWORD:{self.password}
        ROLE:{self.role}
        FIRSTNAME:{self.firstname}
        LASTNAME:{self.lastname}
        PHONE_NUMBER_COUNTRY_CODE:{self.phone_number_country_Code}
        PHONE_NUMBER:{self.phone_number}
    """