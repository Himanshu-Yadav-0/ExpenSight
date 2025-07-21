from pydantic import BaseModel
from datetime import datetime


class ExpenseIn(BaseModel):
    amount: float
    currency: str
    category: str
    date: datetime

class ExpenseOut(BaseModel):
    """A simplified Expense model for nesting in the response."""
    id: int
    amount: float
    currency: str
    category: str
    date: datetime
