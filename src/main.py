from fastapi import FastAPI
from src.api_handler import api_router
from utils.db.session import engine
from utils.db.base import Base
from src.user.models import User
from src.expense.models import Expense
from src.notes.models import Note
from src.config import Config

def create_app() -> FastAPI:
    app = FastAPI(title="Expense Tracker System")
    app.include_router(api_router)
    return app
app = create_app()

Base.metadata.create_all(bind=engine)







#401 - unauthorized, token invalid
#403 - forbidden,that means already create login but you not have permission
#500 - server side error