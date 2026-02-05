from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from datetime import date
from utils.db.base import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    description = Column(String)
    date = Column(Date, default=date.today)
    user_id = Column(Integer, ForeignKey("users.id"))


def __repr__(self):
    return f"""
        Expense Info:
            id:{self.id}
            amount:{self.amount}
            decription:{self.description}
            date:{self.date}
            user_id:{self.user_id}
"""