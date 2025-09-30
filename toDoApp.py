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
    # not yet done (someone else do this pls)
    # check if number valid then confirm then remove
    pass


def confirm(prompt: str) -> bool:
    # idk how to do this rn
    # supposed to ask y/n until valid
    pass


def prompt_int(prompt: str) -> int:
    # this should ask for a number and retry if not number
    # still empty
    pass


def prompt_choice() -> str:
    # user picks 1-4
    valid = {"1", "2", "3", "4"}
    while True:
        ch = input("enter choice: ").strip()
        if ch in valid:
            return ch
        print("please choose 1, 2, 3, or 4.")


def main() -> None:
    while True:
        print("--- To-Do Menu ---")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        ch = prompt_choice()
        if ch == "1":
            t = input("enter task: ")
            if add_task(t):
                show_tasks()
        elif ch == "2":
            show_tasks()
        elif ch == "3":
            show_tasks()
            n = prompt_int("enter task no to remove: ")
            if remove_task(n):
                show_tasks()
        elif ch == "4":
            print("goodbye!")
            break


if __name__ == "__main__":
    main()
