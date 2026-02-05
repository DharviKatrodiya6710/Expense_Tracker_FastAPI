from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from utils.db.session import get_db
from src.expense.schemas import ExpenseCreate, ExpenseUpdate
from src.expense.crud import add_expense,update_expense, delete_expense
from src.user.models import get_current_user

api_router = APIRouter(prefix="/expense", tags=["Expense"])

@api_router.post("/add")
def add(
    expense: ExpenseCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return add_expense(db, expense, user_id=user["user_id"])

@api_router.put("/update/")
def update(
    expense_id: int,
    expense: ExpenseUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return update_expense(db, expense_id, expense, user_id=user["user_id"])


@api_router.delete("/delete/{expense_id}")
def delete(
    expense_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return delete_expense(db, expense_id, user_id=user["user_id"])

#notes

#db: Session = Depends(get_db), that means api fuction work with database
#session = CRUD
#get_current_user = who is ?, token take header and check / verify kre che
#depends = run th function first
