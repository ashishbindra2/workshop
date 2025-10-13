import plotly.express as px
import streamlit as st

import pandas as pd
from pages.dashboard import budget
from pages.user_expense import get_amount_by_category, get_user_expense
from Expense import Expense
from pages.add_expense import expense_file_path

# Load and process expenses
expenses: list[Expense] = get_user_expense(expense_file_path)
amount_by_category = get_amount_by_category(expenses)

df = pd.DataFrame(amount_by_category.items(), columns=["Category", "Amount"])
total_spent = sum(exp.amount for exp in expenses)

# Pie chart of expenses by category
fig = px.pie(
    df, names="Category", values="Amount", title="Spending Distribution by Category"
)
st.plotly_chart(fig, width="stretch",config={"responsive": True})

# Trend over time (optional if dates are stored)
if hasattr(expenses[0], "date"):
    df_trend = pd.DataFrame(
        [
            {"Date": exp.date, "Amount": exp.amount, "Category": exp.category}
            for exp in expenses
        ]
    )
    df_trend["Date"] = pd.to_datetime(df_trend["Date"])
    df_trend = df_trend.groupby("Date")["Amount"].sum().reset_index()

    st.subheader("📈 Spending Over Time")
    fig_trend = px.line(
        df_trend, x="Date", y="Amount", markers=True, title="Daily Spending Trend",
    )
    st.plotly_chart(fig_trend, width="stretch")

# ---------- Budget Progress (Custom Color Bar) ----------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("📊 Budget Usage")

progress = total_spent / budget if budget > 0 else 0
progress_percent = min(progress * 100, 100)

# Choose color based on usage
if progress < 0.8:
    bar_color = "#4CAF50"  # green
elif progress < 1.0:
    bar_color = "#FFC107"  # yellow
else:
    bar_color = "#F44336"  # red

# Custom progress bar with CSS
st.markdown(
    f"""
    <div style="background-color:#e0e0e0;border-radius:15px;overflow:hidden;">
        <div style="
            width:{progress_percent}%;
            background-color:{bar_color};
            height:24px;
            text-align:center;
            line-height:24px;
            color:white;
            font-weight:bold;
        ">
            {progress_percent:.1f}%
        </div>
    </div>
    <p style="margin-top:5px;">
        💸 Spent: <b>₹{total_spent:.2f}</b> / Budget: <b>₹{budget:.2f}</b>
    </p>
""",
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)


fig = px.bar(
    df,
    x="Category",
    y="Amount",
    text="Amount",
    color="Category",
    title="Expenses by Category",
)

# Add ₹ symbol to text labels
fig.update_traces(texttemplate="₹%{text:.2s}", textposition="outside")
fig.update_layout(yaxis=dict(title="Amount (₹)"))

st.plotly_chart(fig, width="stretch")
# st.bar_chart(df.set_index("Category"))
