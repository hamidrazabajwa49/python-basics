# Define the Expense class
class Expense:
    def __init__(self, amount, category, date, description):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def display(self):
        print(f'Amount: {self.amount}')
        print(f'Category: {self.category}')
        print(f'Date: {self.date}')
        print(f'Description: {self.description}')
        print("-" * 30)

    def to_dict(self):
        return {
            'amount': self.amount,
            'category': self.category,
            'date': self.date,
            'description': self.description
        }

    def __str__(self):
        return f'{self.date} | {self.category} | {self.amount} | {self.description}'


# ExpenseManager class
class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)
        print("Expense added successfully!")

    def view_all_expenses(self):
        if not self.expenses:
            print("No expenses to show.")
            return
        for expense in self.expenses:
            expense.display()

    def delete_expense(self, index):
        if 0 <= index - 1 < len(self.expenses):
            removed = self.expenses.pop(index - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid index!")

    def filter_by_category(self, category):
        found = False
        for expense in self.expenses:
            if expense.category.lower() == category.lower():
                expense.display()
                found = True
        if not found:
            print("No expenses found for this category.")

    def filter_by_date(self, date):
        found = False
        for expense in self.expenses:
            if expense.date == date:
                expense.display()
                found = True
        if not found:
            print("No expenses found for this date.")

    def calculate_total(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        total = sum(exp.amount for exp in self.expenses)
        print(f'Total Spending: {total}')


# File Handling
import json
import os

def save_expenses_to_file(manager, filename):
    try:
        with open(filename, 'w') as f:
            data = [expense.to_dict() for expense in manager.expenses]
            json.dump(data, f, indent=4)
        print("Data saved successfully.")
    except Exception as e:
        print("Error saving:", e)

def load_expenses_from_file(manager, filename):
    if not os.path.exists(filename):
        return
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            for item in data:
                exp = Expense(
                    amount=item['amount'],
                    category=item['category'],
                    date=item['date'],
                    description=item['description']
                )
                manager.add_expense(exp)
        print("Expenses loaded.")
    except Exception as e:
        print("Error loading:", e)


# Command-Line Interface
def main():
    manager = ExpenseManager()
    filename = 'expenses.json'
    load_expenses_from_file(manager, filename)

    while True:
        print("\nEXPENSE MANAGER MENU")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Delete Expense")
        print("4. Filter by Category")
        print("5. Filter by Date")
        print("6. Calculate Total Spending")
        print("7. Save & Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                date = input("Enter date (YYYY-MM-DD): ")
                description = input("Enter description: ")
                expense = Expense(amount, category, date, description)
                manager.add_expense(expense)
            except ValueError:
                print("Invalid input for amount.")
        elif choice == '2':
            manager.view_all_expenses()
        elif choice == '3':
            try:
                index = int(input("Enter index to delete (1-based): "))
                manager.delete_expense(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            cat = input("Enter category to filter: ")
            manager.filter_by_category(cat)
        elif choice == '5':
            date = input("Enter date (YYYY-MM-DD): ")
            manager.filter_by_date(date)
        elif choice == '6':
            manager.calculate_total()
        elif choice == '7':
            save_expenses_to_file(manager, filename)
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


# Entry Point
if __name__ == "__main__":
    main()
