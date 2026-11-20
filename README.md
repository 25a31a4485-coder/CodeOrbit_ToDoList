# CodeOrbit Tech Python Programming Internship
## Project 2: To-Do List CLI Application

A beginner-friendly Command-Line Interface (CLI) To-Do List application written in standard Python. This project fulfills all requirements for Project 2 of the CodeOrbit Tech Python Programming Internship.

---

## 📌 Project Overview

The **To-Do List CLI Application** is an interactive, text-based task manager that runs directly in the terminal. It provides an intuitive menu-driven interface to manage everyday tasks, with persistent storage using a plain text file (`tasks.txt`).

---

## ✨ Features

1. **Add Task:**
   - Enter and append new tasks to the list.
   - Validates user input to prevent empty or whitespace-only tasks.
   - Provides clear confirmation messages.

2. **View Tasks:**
   - Displays all tasks in an organized, numbered list (1-indexed).
   - Shows a friendly notice whenever the list is empty.

3. **Remove Task:**
   - Removes tasks using their displayed task number.
   - Shows the current numbered tasks for reference.
   - Provides an option to cancel removal.
   - Validates input for non-numeric values and out-of-range numbers.

4. **In-Memory Storage:**
   - Uses a standard Python `list` to store and manage tasks during program execution.

5. **Modular Architecture:**
   - Structured into clean, separate functions for adding, viewing, removing, saving, and loading tasks.

6. **Continuous Application Loop:**
   - Runs in a loop allowing multiple operations until the user chooses to exit.

7. **File Persistence (Save & Load):**
   - Automatically loads existing tasks from `tasks.txt` upon application startup.
   - Provides an explicit option to save tasks at any time.
   - Automatically saves tasks on exit to prevent accidental data loss.

8. **Robust Input & Error Handling:**
   - Gracefully handles non-numeric and out-of-range menu selections.
   - Handles invalid task indices and non-numeric inputs during task removal.
   - Safe file handling using Python context managers (`with` statements).

9. **Beginner-Friendly & Well-Documented:**
   - Written in simple, readable Python code adhering to PEP 8.
   - Thoroughly commented to explain logic, functions, parameters, and flow.

---

## 📋 Requirements

- **Python**: Version 3.6 or higher.
- **External Libraries**: None! Uses only Python's standard library.
- **Platform**: Cross-platform (Windows, macOS, Linux).

---

## 🚀 How to Run the Application

1. Open your terminal or command prompt (PowerShell, CMD, Bash, etc.).
2. Navigate to the project directory:
   ```bash
   cd c:\Users\venum\OneDrive\Documents\CodeOrbit_ToDoList
   ```
3. Run the application using Python:
   - On Windows (using Python launcher):
     ```bash
     py todo.py
     ```
   - Or standard command:
     ```bash
     python todo.py
     ```
   - On macOS/Linux:
     ```bash
     python3 todo.py
     ```

---

## 💻 Usage Example

```text
Welcome to the CodeOrbit To-Do List Application!
[*] Starting with an empty to-do list.

========================================
      TO-DO LIST CLI APPLICATION        
========================================
  1. Add Task
  2. View Tasks
  3. Remove Task
  4. Save Tasks to File
  5. Exit
========================================
Enter your choice (1-5): 1

--- Add New Task ---
Enter the task description: Complete CodeOrbit Python Internship Project 2
[✓] Task added successfully: 'Complete CodeOrbit Python Internship Project 2'

========================================
      TO-DO LIST CLI APPLICATION        
========================================
  1. Add Task
  2. View Tasks
  3. Remove Task
  4. Save Tasks to File
  5. Exit
========================================
Enter your choice (1-5): 2

========================================
             YOUR TO-DO LIST            
========================================
  1. Complete CodeOrbit Python Internship Project 2
========================================
```

---

## 📁 Project Structure

```text
CodeOrbit_ToDoList/
│
├── todo.py          # Main Python application source code
├── README.md        # Comprehensive project documentation
└── tasks.txt        # Text file for persistent task storage (created on save)
```

---

## 🔍 Function Descriptions

| Function | Description |
| :--- | :--- |
| `load_tasks(filename)` | Reads tasks from the given text file into a Python list on startup. |
| `save_tasks(tasks, filename)` | Writes all current tasks from memory to the text file. |
| `view_tasks(tasks)` | Displays all tasks numbered starting from 1 or shows an empty list message. |
| `add_task(tasks)` | Prompts for a new task string, validates it, and appends it to the list. |
| `remove_task(tasks)` | Shows tasks, prompts for a task number to delete, validates index, and removes it. |
| `display_menu()` | Prints the formatted user menu with options 1 through 5. |
| `main()` | Initializes the app, orchestrates the menu loop, and handles user navigation. |

---

## 🎓 Internship Information

- **Organization**: CodeOrbit Tech
- **Program**: Python Programming Internship
- **Project**: Project 2 - To-Do List CLI Application
- **Language**: Python 3
