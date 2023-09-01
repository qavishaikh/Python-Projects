# Expence Tracker App 
expenses = []

def add_expense():
    category = input("Enter the category: ")
    date = input("Enter the date (YYYY-MM-DD): ")
    amount = float(input("Enter the amount in PKR: "))
    expense = (category, date, amount)
    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses to display.")
    else:
        print("All Expenses:")
        for idx, (category, date, amount) in enumerate(expenses, start=1):
            print(f"{idx}. Category: {category}, Date: {date}, Amount: ₨{amount:.2f}")  # Use ₨ for PKR

def total_expenses_by_category():
    category_totals = {}
    for category, _, amount in expenses:
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    print("\nTotal Expenses by Category:")
    for category, total in category_totals.items():
        print(f"{category}: ₨{total:.2f}") 

while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Total Expenses by Category")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expenses_by_category()
    elif choice == "4":
        print("Goodbye!","\n Created By Qavi")
        break
    else:
        print("Invalid choice. Please try again.")
