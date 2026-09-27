from Expense import Expense
from datetime import datetime
from calendar import monthrange


def main():
    print(f"🏃‍♀️ Running Expense Tracker!")

    expense_file_path = "expense.csv"
    budget = 2000
    # # Get user input for expense
    expense = get_user_expense()
    # print(expense)
    # # write their expense to a file.
    save_expense_to_file(expense, expense_file_path)

    # Read file and summarize expenses.
    summarize_expenses(expense_file_path, budget)


def get_user_expense():
    print("Getting User Expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))

    # print(f"You've entered {expense_name}, {expense_amount}")

    expense_categories = {
        1: "🍔 Food",
        2: "🏠 Home",
        3: "💼 Work",
        4: "🎭 Fun",
        5: "🎶 Misc",
    }

    while True:
        print("Select a category")

        for i, category_name in expense_categories.items():
            print(f" {i}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: "))

        if selected_index in range(1, len(expense_categories) + 1):
            new_expense = Expense(
                name=expense_name, amount=expense_amount, category=expense_categories[i]
            )
            return new_expense
        else:
            print("Invalid category, Please try again!")


def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving User Expense: {expense} to {expense_file_path}")

    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")


def summarize_expenses(expense_file_path, budget):
    print(f"Summarizing User Expense")

    expenses: list[Expense] = []
    with open(expense_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.split(",")
            line_expense = Expense(
                expense_name, expense_category, float(expense_amount)
            )
            print(line_expense)
            expenses.append(line_expense)
    print(expenses)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category

        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print(amount_by_category)

    print("Expense By Category :")

    for key, amount in amount_by_category.items():
        print(f"   {key}: ${amount:.2f}")

    total_spend = sum([x.amount for x in expenses])
    print(f"Total spent ${total_spend:.2f} this month!")

    remaining_buget = budget - total_spend
    print(f"Buget Remaning: ${remaining_buget:.2f}")

    #  Buget per day
    now = datetime.now()
    days_in_month = monthrange(now.year, now.month)[1]
    remaning_days = days_in_month - now.day

    print("Remaing days in the current month:", remaning_days)

    daily_budget = remaining_buget / remaning_days
    print(f"Budget Per Day: ${daily_budget:.2f}")

def buget_per_day():
    pass
if __name__ == "__main__":
    main()
