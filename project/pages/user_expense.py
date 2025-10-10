import streamlit as st
from Expense import Expense
from datetime import datetime
from calendar import monthrange


def budget_per_day():
    now = datetime.now()
    days_in_month = monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    return remaining_days if remaining_days > 0 else 1  # Avoid division by zero

def get_user_expense(file_path):
    expenses: list[Expense] = []
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            expense = Expense(expense_name, expense_category, float(expense_amount))
            expenses.append(expense)
    return expenses

def get_amount_by_category(expenses):
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        amount_by_category[key] = amount_by_category.get(key, 0) + expense.amount
    return amount_by_category
