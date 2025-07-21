from fastapi import HTTPException
from app.database.db import prisma
from app.schemas.expense_schema import ExpenseIn
from datetime import datetime

async def get_all_expenses(current_user):
    """
    Fetches all expenses linked to the currently authenticated user.
    """
    if not current_user:
        raise HTTPException(status_code=401, detail="Not Authenticated")
    
    expense_list = await prisma.expense.find_many(
        where={
            'userId': current_user.id
        },
        order={
            'date': 'desc' 
        }
    )
    return expense_list

async def add_expense_manually(expense:ExpenseIn,current_user):
    if not current_user:
        raise HTTPException(status_code=401, detail="Not Authenticated")
    
    ex = await prisma.expense.create(
        data={
            'amount': expense.amount,
                'currency': expense.currency,
                'category': expense.category,
                'date': datetime.now(),
                'userId':current_user.id
        }
    )
    return ex