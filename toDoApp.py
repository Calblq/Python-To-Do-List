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
        ans = input(prompt).strip().lower()
        if ans in {"y", "yes"}:
            return True
        elif ans in {"n", "no"}:
            return False
        else:
            print("please enter y/n")


def prompt_int(prompt: str) -> int:
    # this should ask for a number and retry if not number
    while True:
        val = input(prompt).strip()
        if val.isdigit():
            return int(val)
        else:
            print("please enter a valid number")
