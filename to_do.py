tasks = []
# 1. add task
# 2. view tasks
# 3. delete task
# 4. exit

def add_task():
    str = input("Enter task you want to add: ")
    tasks.append(str)
    print("Task added successfully")

def view_task():
    if len(tasks) == 0:
        print("No tasks available")
    else:
        for i in range(len(tasks)):
            print(f"{i+1}.{tasks[i]}")

def delete_task():
    view_task()

    if len(tasks) == 0:
        return

    task_number = int(input("Enter the task number to delete:"))

    if 1 <= task_number <= len(tasks):
        tasks.pop(task_number-1)
        print("Task deleted successfully")
    else:
        print("Invalid task number")

def main():
    while True:
        print("\n---TO-DO APP---")
        print("1. Add task")
        print("2. View task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main()
        


