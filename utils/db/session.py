from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.db.base import Base

DATABASE_URL = "postgresql://postgres:dharvi@localhost:5432/Expense_Tracker_System"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#engine - manage database using gateway