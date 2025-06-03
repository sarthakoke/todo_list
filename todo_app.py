import json  # For saving/loading tasks to/from a JSON file

# Global list to store tasks
tasks = []

# Load tasks from the JSON file (if it exists)
def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []

# Save current tasks to the JSON file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

# Show the menu options
def show_menu():
    print("\nTO-DO LIST MENU")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Mark as Done")
    print("5. Mark as Not Done")
    print("6. Exit")

# Display all tasks with their status (done or not done)
def view_tasks():
    if not tasks:
        print("There are no tasks.")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "✅" if task["done"] else "❌"
            print(f"{idx}. {task['task']} - {status}")

# Add a new task to the list
def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "done": False})
    print("Task added.")
    save_tasks()

# Delete a task by its number
def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Deleted: {removed['task']}")
            save_tasks()
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")

# Mark a task as done
def mark_done():
    view_tasks()
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print("Marked as done.")
            save_tasks()
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")

# Mark a task as not done
def mark_notdone():
    view_tasks()
    try:
        num = int(input("Enter task number to mark as not done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = False
            print("Marked as not done.")
            save_tasks()
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")

# Load existing tasks before starting the menu loop
load_tasks()

# Main menu loop
while True:
    show_menu()
    choice = input("Choose an option (1–6): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        mark_done()
    elif choice == '5':
        mark_notdone()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
