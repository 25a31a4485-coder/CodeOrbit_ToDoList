"""
CodeOrbit Tech Python Programming Internship
Project 2: To-Do List CLI Application
Author: Intern
File: todo.py

A beginner-friendly Command-Line Interface (CLI) To-Do List application.
Allows users to add, view, remove, and persist tasks in a text file without
using any external libraries.
"""

import os

# Default file name used to store tasks
DATA_FILE = "tasks.txt"


def load_tasks(filename=DATA_FILE):
    """
    Load tasks from a text file into a Python list.
    If the file does not exist, returns an empty list.
    """
    tasks = []
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                for line in file:
                    task = line.strip()
                    # Only add non-empty lines
                    if task:
                        tasks.append(task)
        except Exception as error:
            print(f"[!] Warning: Could not read '{filename}': {error}")
    return tasks


def save_tasks(tasks, filename=DATA_FILE):
    """
    Save the current tasks list into a text file.
    Each task is written on a new line.
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(task + "\n")
        print(f"[✓] Tasks successfully saved to '{filename}'.")
        return True
    except Exception as error:
        print(f"[!] Error: Could not save tasks to '{filename}': {error}")
        return False


def view_tasks(tasks):
    """
    Display all tasks in a numbered list.
    Displays a friendly message if the list is empty.
    """
    print("\n" + "=" * 40)
    print("             YOUR TO-DO LIST            ")
    print("=" * 40)

    if not tasks:
        print("Your to-do list is empty! No tasks to show.")
        print("Add a new task using Option 1.")
    else:
        # Loop through tasks and display each with a 1-based number
        for index, task in enumerate(tasks, start=1):
            print(f"  {index}. {task}")

    print("=" * 40)


def add_task(tasks):
    """
    Prompt the user to enter a new task and add it to the tasks list.
    Validates that the task is not empty or just whitespace.
    """
    print("\n--- Add New Task ---")
    new_task = input("Enter the task description: ").strip()

    # Validate user input
    if not new_task:
        print("[!] Task cannot be empty. Please enter a valid task.")
        return

    # Add the valid task to the list
    tasks.append(new_task)
    print(f"[✓] Task added successfully: '{new_task}'")


def remove_task(tasks):
    """
    Prompt the user for a task number and remove that task from the list.
    Handles invalid inputs (non-numeric, out-of-range).
    """
    print("\n--- Remove Task ---")

    # Check if there are tasks to remove
    if not tasks:
        print("[!] No tasks available to remove. Your list is already empty.")
        return

    # Display current tasks so the user can easily see task numbers
    print("Current tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"  {index}. {task}")

    user_input = input("\nEnter the task number to remove (or press Enter to cancel): ").strip()

    # Allow user to cancel removal
    if not user_input:
        print("[-] Task removal cancelled.")
        return

    # Validate that the user entered a valid number
    try:
        task_number = int(user_input)
    except ValueError:
        print("[!] Invalid input: Please enter a valid whole number.")
        return

    # Check if the number is within the valid range
    if 1 <= task_number <= len(tasks):
        # Convert 1-based task number to 0-based list index
        removed_task = tasks.pop(task_number - 1)
        print(f"[✓] Task #{task_number} ('{removed_task}') was successfully removed.")
    else:
        print(f"[!] Invalid task number. Please enter a number between 1 and {len(tasks)}.")


def display_menu():
    """
    Display the main menu options to the user.
    """
    print("\n" + "=" * 40)
    print("      TO-DO LIST CLI APPLICATION        ")
    print("=" * 40)
    print("  1. Add Task")
    print("  2. View Tasks")
    print("  3. Remove Task")
    print("  4. Save Tasks to File")
    print("  5. Exit")
    print("=" * 40)


def main():
    """
    Main application loop.
    Controls execution flow, handles menu navigation, and exits cleanly.
    """
    print("Welcome to the CodeOrbit To-Do List Application!")

    # Load previously saved tasks from file into a Python list
    tasks = load_tasks(DATA_FILE)
    if tasks:
        print(f"[*] Loaded {len(tasks)} existing task(s) from '{DATA_FILE}'.")
    else:
        print("[*] Starting with an empty to-do list.")

    # Main application loop
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            save_tasks(tasks, DATA_FILE)
        elif choice == "5":
            # Auto-save before exiting to prevent data loss
            save_tasks(tasks, DATA_FILE)
            print("\nThank you for using the To-Do List Application. Goodbye!\n")
            break
        else:
            print("[!] Invalid choice! Please select an option between 1 and 5.")


# Run the application only if executed directly
if __name__ == "__main__":
    main()
