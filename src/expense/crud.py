from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.expense.models import Expense

def add_expense(db, expense, user_id):
    new = Expense(
        amount=expense.amount,
        description=expense.description,
        date=expense.date,
        user_id=user_id
    )
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


def update_expense(db: Session, expense_id: int, expense, user_id: int):
    db_exp = db.query(Expense).filter(
        Expense.id == expense_id,
        Expense.user_id == user_id
    ).first()

    if not db_exp:
        raise HTTPException(404, "Expense not found")

    if expense.amount is not None:
        db_exp.amount = expense.amount
    if expense.description is not None:
        db_exp.description = expense.description
    if expense.date is not None:
        db_exp.date = expense.date

    db.commit()
    return {"message": "Expense updated"}


def delete_expense(db: Session, expense_id: int, user_id: int):
    db_exp = db.query(Expense).filter(
        Expense.id == expense_id,
        Expense.user_id == user_id
    ).first()

    if not db_exp:
        raise HTTPException(404, "Expense not found")

    db.delete(db_exp)
    db.commit()
    return {"message": "Expense deleted"}

#notes

# remember dharvi

#401 - unauthorized, token invalid
#403 - forbidden - that means already create login but you not have permission
#500 - server side error
#200 - request OK
#201 - create
#400 - bad request - wrong data 

# filter() - to data get in database