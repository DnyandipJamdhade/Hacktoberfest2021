# todo_list.py

tasks = []

def show_tasks():
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

while True:
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter a new task: ")
        tasks.append(task)
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        show_tasks()
        num = int(input("Enter task number to remove: "))
        if 0 < num <= len(tasks):
            tasks.pop(num - 1)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
