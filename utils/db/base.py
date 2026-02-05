from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)



Base = declarative_base()


#notes

#base = declarative_base() - that means database create base class on model