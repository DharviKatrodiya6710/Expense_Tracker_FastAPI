from fastapi import FastAPI
from api_handler import api_router
from utils.db.base import Base
from utils.db.session import engine
from src.users.models import User
from src.expense.models import Expense


app = FastAPI(title="Expense Tracker System")

Base.metadata.create_all(bind=engine)

app.include_router(api_router)


#401 - unauthorized, token invalid
#403 - forbidden,that means already create login but you not have permission
#500 - server side error