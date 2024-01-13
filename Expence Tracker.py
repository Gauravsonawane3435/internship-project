import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, description, category):
        expense = {
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'amount': amount,
            'description': description,
            'category': category
        }
        self.expenses.append(expense)

    def save_expenses(self):
        with open('expenses.json', 'w') as file:
            json.dump(self.expenses, file)

    def load_expenses(self):
        try:
            with open('expenses.json', 'r') as file:
                self.expenses = json.load(file)
        except FileNotFoundError:
            pass

    def get_monthly_summary(self):
        # Implement logic for monthly summary
        pass

    def get_category_summary(self):
        # Implement logic for category-wise expenditure
        pass

# Example Usage:
tracker = ExpenseTracker()
tracker.load_expenses()

while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. Monthly Summary")
    print("3. Category-wise Summary")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        amount = float(input("Enter the amount spent: "))
        description = input("Enter a brief description: ")
        category = input("Enter the expense category: ")

        tracker.add_expense(amount, description, category)
        tracker.save_expenses()
        print("Expense added successfully!")

    elif choice == '2':
        tracker.get_monthly_summary()
        # Display monthly summary

    elif choice == '3':
        tracker.get_category_summary()
        # Display category-wise summary

    elif choice == '4':
        print("Exiting Expense Tracker. Have a great day!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
