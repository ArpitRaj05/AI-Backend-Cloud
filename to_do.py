import json

tasks = []
# 1. add task
# 2. view tasks
# 3. delete task
# 4. exit

def save_tasks():
    with open("tasks.json","w") as file:
        json.dump(tasks,file,indent=4)

def load_tasks():
    global tasks

    try:
        with open("tasks.json","r") as file:
            tasks = json.load(file)

    except(FileNotFoundError, json.JSONDecodeError):
        tasks = []


def get_task_number():
    try:
        task_number = int(input("Enter task number: "))
    except ValueError:
        print("Please enter a valid number.")
        return None

    if 1 <= task_number <= len(tasks):
        return task_number
    else:
        print("Invalid task number.")
        return None


def add_task():
    task = input("Enter task you want to add: ")
    tasks.append({
        "title": task,
        "completed": False
    })
    save_tasks()
    print("Task added successfully")

def view_task():
    if len(tasks) == 0:
        print("No tasks available")
    else:
        for i in range(len(tasks)):
            status = "Completed" if tasks[i]["completed"] else "Pending"
            print(f"{i+1}.{tasks[i]['title']} - {status}")

def complete_task():
    view_task()

    if len(tasks) == 0:
        return

    task_number = get_task_number()

    if task_number is None:
        return

    if 1 <= task_number <= len(tasks):
        tasks[task_number-1]["completed"] = True
        print("Task marked as completed")
    else:
        print("Invalid task number")

    save_tasks()

def delete_task():
    view_task()

    if len(tasks) == 0:
        return
    
    task_number = get_task_number()

    if task_number is None:
        return

    if 1 <= task_number <= len(tasks):
        tasks.pop(task_number-1)
        print("Task deleted successfully")
    else:
        print("Invalid task number")

    save_tasks()

def main():
    while True:
        print("\n---TO-DO APP---")
        print("1. Add task")
        print("2. View task")
        print("3. Delete task")
        print("4. Mark task as Completed")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

load_tasks()
main()
        


