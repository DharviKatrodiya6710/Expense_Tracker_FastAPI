from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from utils.db.session import get_db
from src.expense.schemas import ExpenseCreate, ExpenseUpdate, ExpenseOut
from src.expense.crud import add_expense,update_expense, delete_expense
from src.user.auth import get_current_user

api_router = APIRouter(prefix="/expense", tags=["Expense"])

@api_router.post("/add", response_model=ExpenseOut)
def add(
    expense: ExpenseCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return add_expense(db, expense, user.id)

@api_router.put("/update/")
def update(
    expense_id: int,
    expense: ExpenseUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    updated = update_expense(db, expense_id, expense, user_id=user.id)
    if not updated:
        raise HTTPException(status_code=404, detail="Expense not found")
    return updated

@api_router.delete("/delete/{expense_id}")
def delete(
    expense_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    deleted = delete_expense(db, expense_id, user_id=user.id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Expense not found")
    return deleted


#notes

#db: Session = Depends(get_db), that means api fuction work with database
#session = CRUD
#get_current_user = who is ?, token take header and check / verify kre che
#depends = run th function first
