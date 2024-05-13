def record_expense(expenses):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    expenses.setdefault(category, 0)
    expenses[category] += amount
    print("Expense recorded successfully!")

def visualize_spending(expenses):
    if not expenses:
        print("No expenses recorded yet!")
        return
    
    categories = list(expenses.keys())
    amounts = list(expenses.values())
    
    import matplotlib.pyplot as plt
    plt.figure(figsize=(8, 6))
    plt.bar(categories, amounts, color='skyblue')
    plt.xlabel('Expense Categories')
    plt.ylabel('Amount Spent')
    plt.title('Monthly Spending Summary')
    plt.xticks(rotation=45)
    plt.show()

def main():
    expenses = {}
    
    while True:
        print("\n===== Budget Tracker Menu =====")
        print("1. Record Expense")
        print("2. Visualize Spending")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            record_expense(expenses)
        elif choice == '2':
            visualize_spending(expenses)
        elif choice == '3':
            print("Exiting the Budget Tracker. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
