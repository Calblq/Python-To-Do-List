# toDoApp.py

tasks=[]

def confirm(prompt: str) -> bool:
    "Ask yes/no; return True for yes."
    while True:
        ans = input(prompt).strip().lower()
        if ans in {"y", "yes"}:
            return True
        if ans in {"n", "no"}:
            return False
        print("please type y or n.")


def prompt_int(prompt: str) -> int:
    "Prompt for an integer, retrying on invalid input."
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("please enter a number (e.g., 1, 2, 3)")


def addtask(task) :
  tasks.append(task)
  print("task added!")

def showTasks( ):
    if len(tasks)==0 :
      print("no tasks yet")
    else:
     for i in range (len(tasks)):
      print(i+1,".",tasks[i])

def removetask(tasknumber):
    tasks.pop(tasknumber) 
    print("task removed!!")

def main():
    while True:
        print("1 Add Task")
        print("2.Show Tasks")
        print("3.Remove Task")
        print("4- Exit")
        ch = input("enter choice : ")
        if ch=="1":
            t = input("enter task : ")
            addtask(t)
        elif ch=="2":
            showTasks()
        elif ch=="3":
            n=int(input("enter task no to remove: "))
            removetask(n)   
        elif ch=="4":
            break;
        else:
            print("wrong choice!!")
main()
