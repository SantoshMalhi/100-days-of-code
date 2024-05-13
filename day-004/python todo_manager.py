# Define a function to display the main menu
def display_menu():
    print("Welcome to the To-Do List Manager!")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Save and Quit")

# Define a function to load tasks from a file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

# Define a function to save tasks to a file
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Main function to manage the To-Do List
def main():
    tasks = load_tasks()  # Load tasks from file
    
    while True:
        display_menu()  # Display the main menu
        choice = input("Enter your choice: ")

        if choice == "1":  # View Tasks
            print("\nTasks:")
            if tasks:
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")
            else:
                print("No tasks yet.")

        elif choice == "2":  # Add Task
            task = input("Enter the task: ")
            tasks.append(task)
            print("Task added successfully!")

        elif choice == "3":  # Mark Task as Completed
            if tasks:
                print("Select task to mark as completed:")
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")
                task_index = int(input()) - 1
                if 0 <= task_index < len(tasks):
                    del tasks[task_index]
                    print("Task marked as completed!")
                else:
                    print("Invalid task number.")
            else:
                print("No tasks to mark.")

        elif choice == "4":  # Save and Quit
            save_tasks(tasks)
            print("Tasks saved successfully. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  # Execute the main function
