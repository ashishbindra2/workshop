import streamlit as st
from Expense import Expense

st.header("💸 Add Expense Here...")

expense_file_path = "expense.csv"
expense_name = st.text_input(
    "Enter expense name: ", placeholder="Type your expense here..."
)
expense_amount = st.number_input("Enter expense amount: ")

expense_categories = ["🍔 Food", "🏠 Home", "💼 Work", "🎭 Fun", "🎶 Misc"]

selected_index = st.selectbox(f"Select a category number : ", expense_categories)

new_expense: Expense = None
if expense_name and expense_amount > 0:
    new_expense = Expense(
        name=expense_name, amount=expense_amount, category=selected_index
    )
    "print", new_expense


btn_submit = st.button("Add")


if btn_submit:

    if expense_name and expense_amount > 0:
        with open(expense_file_path, "a", encoding="utf-8") as f:
            f.write(f"{new_expense.name},{new_expense.amount},{new_expense.category}\n")

        st.success(f"✅ Saved: {new_expense} to {expense_file_path}")
    else:
        st.error("⚠️ Please enter a valid expense name and amount before saving.")
