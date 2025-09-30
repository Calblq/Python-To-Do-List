tasks: list[str] = []


def add_task(title: str) -> bool:
    # adds a task if not empty
    title = title.strip()
    if not title:
        print("task cannot be empty.")
        return False
    tasks.append(title)
    print(f'added: "{title}"')
    return True


def show_tasks() -> None:
    # just shows the list of tasks
    if not tasks:
        print("no tasks yet")
        return
    for i, t in enumerate(tasks, start=1):
        print(f"{i}. {t}")


def remove_task(task_number: int) -> bool:
    # check if number valid then confirm then remove
    if task_number < 1 or task_number > len(tasks):
        print("invalid task number")
        return False

    task = tasks[task_number - 1]
    if confirm(f'Do you want to remove "{task}"? (y/n): '):
        tasks.pop(task_number - 1)
        print(f'removed: "{task}"')
        return True
    else:
        print("task not removed")
        return False


def confirm(prompt: str) -> bool:
    # supposed to ask y/n until valid
    while True:
        choice = input(prompt).strip().lower()
        if choice in {"y", "yes"}:
            return True
        elif choice in {"n", "no"}:
            return False
        else:
            print("please enter y/n")


def prompt_int(prompt: str) -> int:
    # this should ask for a number and retry if not number
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        else:
            print("please enter a valid number")


def prompt_choice() -> str:
    # user picks 1-4
    valid = {"1", "2", "3", "4"}
    while True:
        choice = input("enter choice: ").strip()
        if choice in valid:
            return choice
        print("please choose 1, 2, 3, or 4.")


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
            print("goodbye!")
            break


if __name__ == "__main__":
    main()