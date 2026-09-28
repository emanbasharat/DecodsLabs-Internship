def add_task(tasks):
    task = input("Enter your task: ")

    if task.strip() != "":
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")


def view_tasks(tasks):
    print("\n===== YOUR TASKS =====")

    if len(tasks) == 0:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


def main():
    tasks = []

    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")


main()

