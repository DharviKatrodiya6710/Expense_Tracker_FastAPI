from fastapi import APIRouter
from src.user.api import api_router as users_router
from src.expense.api import api_router as expense_router
from src.notes.api import api_router as notes_router


api_router = APIRouter()

api_router.include_router(users_router)
api_router.include_router(expense_router)
api_router.include_router(notes_router)