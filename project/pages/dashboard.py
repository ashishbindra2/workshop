import streamlit as st
import pandas as pd

from pages.user_expense import get_amount_by_category, get_user_expense, budget_per_day
from pages.add_expense import expense_file_path
from Expense import Expense

# ---------- Dashboard Header ----------
st.markdown(
    "<h1 style='text-align:center;'>📊 Personal Expense Dashboard</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align:center;color:gray;'>Track your expenses, budgets, and financial health.</p>",
    unsafe_allow_html=True,
)

# Sidebar for inputs
st.sidebar.header("⚙️ Settings")
budget = st.sidebar.number_input("Set Your Monthly Budget:", value=2000)

# Load and process expenses
expenses: list[Expense] = get_user_expense(expense_file_path)
amount_by_category = get_amount_by_category(expenses)

# Summary Section
total_spent = sum(exp.amount for exp in expenses)

# ---------- Metrics Section ----------

remaining_budget = budget - total_spent
remaining_days = budget_per_day()
daily_budget = remaining_budget / remaining_days if remaining_days > 0 else 0

col1, col2, col3 = st.columns(3)

col1.metric("💸 Total Spent", f"₹{total_spent:.2f}")
col2.metric(
    "💰 Remaining Budget",
    f"₹{remaining_budget:.2f}",
    delta=f"{(remaining_budget/budget)*100:.1f}% left",
)
col3.metric("📆 Daily Budget", f"₹{daily_budget:.2f}", f"{remaining_days} days left")

# ---------- Table Section ----------

st.subheader("📂 Expenses by Category")
df = pd.DataFrame(amount_by_category.items(), columns=["Category", "Amount"])

# Make index start from 1
df.index = df.index + 1
df.index.name = "S.No"  # Optional: name of index
st.dataframe(df, width="stretch")

# Highlight overspending
if remaining_budget < 0:
    st.error("⚠️ You have exceeded your budget!")
elif remaining_budget < budget * 0.2:
    st.warning("⚠️ Your budget is running low. Be cautious!")
else:
    st.success("✅ You are within your budget. Keep it up!")
