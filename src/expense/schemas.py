from pydantic import BaseModel
from datetime import date as d
from typing import Optional

class ExpenseCreate(BaseModel):
    amount: float
    description: str
    date: d

class ExpenseUpdate(BaseModel):
    amount: Optional[float] = None
    description: Optional[str] = None
    date: Optional[d] = None
