tasks: list[str] = []


def add_task(title: str) -> bool:
    # adds a task if not empty
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
    # just shows the list of tasks
    if not tasks:   
        print("No tasks yet")
        return
    for i, t in enumerate(tasks, start=1):
        print(f"{i}. {t}")


def remove_task(task_number: int) -> bool:
    # check if number valid then confirm then remove
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
    # supposed to ask y/n until valid
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
    # this should ask for a number and retry if not number
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
    # user picks 1-4
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