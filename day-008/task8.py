import matplotlib.pyplot as plt
import pandas as pd

class BudgetTracker:
    def __init__(self):
        self.expenses = {}

    def record_expense(self):
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: "))
        self.expenses.setdefault(category, 0)
        self.expenses[category] += amount
        print("Expense recorded successfully!")

    def visualize_spending(self):
        if not self.expenses:
            print("No expenses recorded yet!")
            return
        
        df = pd.DataFrame(list(self.expenses.items()), columns=['Category', 'Amount'])
        df.plot(kind='bar', x='Category', y='Amount', color='skyblue')
        plt.xlabel('Expense Categories')
        plt.ylabel('Amount Spent')
        plt.title('Monthly Spending Summary')
        plt.xticks(rotation=45)
        plt.show()

    def main_menu(self):
        while True:
            print("\n===== Budget Tracker Menu =====")
            print("1. Record Expense")
            print("2. Visualize Spending")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.record_expense()
            elif choice == '2':
                self.visualize_spending()
            elif choice == '3':
                print("Exiting the Budget Tracker. Have a great day!")
                break
            else:
                print("Invalid choice. Please try again.")

def sample_output():
    tracker = BudgetTracker()

    # Sample expenses
    tracker.expenses = {
        'Groceries': 250,
        'Utilities': 120,
        'Entertainment': 80,
        'Transportation': 50,
        'Dining': 150
    }

    # Visualize spending
    tracker.visualize_spending()

if __name__ == "__main__":
    sample_output()
