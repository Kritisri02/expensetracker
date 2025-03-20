class Expense:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("Expense removed successfully")
        else:
            print("Invalid index")

    def view_expenses(self):
        if len(self.expenses) == 0:
            print("No expenses to display")
        else:
            print("expense list:")
            for i, expense in enumerate(self.expenses, start=1):
                print(f"{i}. Date: {expense.date}, Description: {expense.description}, Amount: ${expense.amount:.2f}")

    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Expenses: ${total:.2f}")


def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Remove expense")
        print("3. view expense")
        print("4. Total expense")
        print("5. exit")

        choice = input("Enter your choice")

        if choice == "1":
            date = input("Enter date:")
            description = input("Enter description:")
            amount = float(input("Enter amount:"))
            expense = Expense(date, description, amount)
            tracker.add_expense(expense)

        elif choice == "2":
            index = int(input("Enter index of expense to remove:"))
            tracker.remove_expense(index)
        elif choice == "3":
            tracker.view_expenses()
        elif choice == "4":
            tracker.total_expenses()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()