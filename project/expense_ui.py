import streamlit as st
# Sidebar header/title
with st.sidebar:
    st.title("💸 Expense Tracker")

# Define navigation pages with icons
pages = {
    "Expense": [
        st.Page("pages/dashboard.py", title="📊 Dashboard"),
        st.Page("pages/add_expense.py", title="➕ Add Expense"),
        st.Page("pages/summarize_expenses.py", title="📈 summarize Expense"),
    ],
}

# Navigation menu
pg = st.navigation(pages)
pg.run()
