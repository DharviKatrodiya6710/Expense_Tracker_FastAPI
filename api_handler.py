from fastapi import APIRouter
from src.user.api import api_router as user_router
from src.expense.api import api_router as expense_router

api_router = APIRouter()
api_router.include_router(user_router)
api_router.include_router(expense_router)
