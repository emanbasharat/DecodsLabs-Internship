# 📝 Python To-Do List

A simple command-line **To-Do List application built using Python**. This project allows users to add tasks, view their tasks, and exit the program through a simple menu.

## ✨ Features

* Add new tasks
* View all saved tasks
* Prevent empty tasks from being added
* Automatically number tasks
* Simple menu-based interface
* Handle invalid choices
* Exit the program easily

## 🛠️ Technologies Used

* Python 3
* Lists
* Functions
* `if-elif-else`
* `while` loop
* `input()`
* `append()`
* `enumerate()`
* String `strip()`

## 📂 Project Structure

```text
Python-To-Do-List/
│
├── todo.py
└── README.md
```

## ⚙️ How the Program Works

### 1. Add Task

The `add_task()` function asks the user to enter a task.

If the task is not empty, it is added to the `tasks` list.

```python
tasks.append(task)
```

If the user enters an empty task, the program displays:

```text
Task cannot be empty.
```

### 2. View Tasks

The `view_tasks()` function displays all the tasks stored in the list.

The `enumerate()` function is used to number the tasks starting from 1.

```python
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")
```

If there are no tasks, the program displays:

```text
No tasks available.
```

### 3. Main Menu

The `main()` function displays the main menu:

```text
===== TO-DO LIST =====
1. Add Task
2. View Tasks
3. Exit
```

The user selects an option by entering `1`, `2`, or `3`.

### 4. Exit

When the user selects option `3`, the program displays:

```text
Goodbye!
```

The `break` statement then stops the loop and ends the program.

## ▶️ How to Run

1. Install **Python 3**.
2. Download or clone this repository.
3. Open the project in VS Code or any Python IDE.
4. Run the Python file:

```bash
python todo.py
```

## 💻 Example

```text
===== TO-DO LIST =====
1. Add Task
2. View Tasks
3. Exit

Enter your choice: 1
Enter your task: Complete Python assignment
Task added successfully!

===== TO-DO LIST =====
1. Add Task
2. View Tasks
3. Exit

Enter your choice: 2

===== YOUR TASKS =====
1. Complete Python assignment
```

## 🎯 Learning Objectives

This project was created to practice basic Python programming concepts, including:

* Functions
* Lists
* Loops
* Conditional statements
* User input
* String methods
* Adding items to a list
* Task numbering

## 🚀 Future Improvements

The project can be improved by adding:

* Delete task option
* Edit task option
* Mark task as completed
* Save tasks permanently in a file
* Search tasks
* Add deadlines or priorities

## 👩‍💻 Author

**Emaan Basharat**

A beginner Python project created for programming practice and internship learning.
