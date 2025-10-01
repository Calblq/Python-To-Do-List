"""
A simple command-line to-do list application.
Users can add, view, and remove tasks.
"""

tasks: list[str] = []


def add_task(title: str) -> bool:
    """" Adds a new task if it is valid, not empty and not a duplicate.
    Returns: bool - True if the task was added, False otherwise. """

    title = title.strip()
    if not title:
        print("Task cannot be empty.")
        return False
    if any(t.lower() == title.lower() for t in tasks):
        print("Task already exists.")
        return False
    tasks.append(title)
    print(f'Added: "{title}"')
    return True


def show_tasks() -> None:
    """ Displays all tasks in the task list with numbering. 
    If no tasks exist, informs the user through a message. """

    if not tasks:
        print("No tasks yet")
        return
    for i, t in enumerate(tasks, start=1):
        print(f"{i}. {t}")


def remove_task(task_number: int) -> bool:
    """Removes a task by its number after user confirmation.
    Returns: bool - True if the task was removed, False otherwise."""

    if not tasks:
        print("No tasks to remove")
        return False
    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number")
        return False

    task = tasks[task_number - 1]
    if confirm(f'Do you want to remove "{task}"? (y/n): '):
        tasks.pop(task_number - 1)
        print(f'Removed: "{task}"')
        return True
    else:
        print("Task not removed")
        return False


def confirm(prompt: str) -> bool:
    """Prompts the user for a yes/no confirmation until valid input is received.
    returns: bool - True for 'yes', False for 'no'."""

    while True:
        choice = input(prompt).strip().lower()
        if not choice:
            print("Input cannot be empty.")
            continue
        if choice in {"y", "yes"}:
            return True
        elif choice in {"n", "no"}:
            return False
        else:
            print("Please enter Y/N")


def prompt_int(prompt: str) -> int:
    """Prompt the user for an interger input until a valid integer is received.
    Returns: int - valid interger input from the user."""

    while True:
        value = input(prompt).strip()
        if not value:
            print("Input cannot be empty.")
            continue
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid number")


def prompt_choice() -> str:
    """Prompt the user to choose a menu option (1-4) until a valid choice is made.
    Returns: str - the choice as a string. """
    valid = {"1", "2", "3", "4"}
    while True:
        choice = input("enter choice: ").strip()
        if not choice:
            print("Input cannot be empty.")
            continue
        if choice in valid:
            return choice
        print("Please choose 1, 2, 3, or 4.")


def main() -> None:
    """Main function for the to do app
    Displays the main menu, handles user input and calls 
    the appropriate functions until exit is chosen."""
    while True:
        print("--- To-Do Menu ---")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        menu_choice = prompt_choice()
        if menu_choice == "1":
            task = input("enter task: ")
            if add_task(task):
                show_tasks()
        elif menu_choice == "2":
            show_tasks()
        elif menu_choice == "3":
            show_tasks()
            task_number = prompt_int("enter task no to remove: ")
            if remove_task(task_number):
                show_tasks()
        elif menu_choice == "4":
            if confirm("Are you sure you want to exit? (y/n): "):
                print("goodbye!")
            break


if __name__ == "__main__":
    main()
