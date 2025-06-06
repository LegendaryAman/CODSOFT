def ToDo_list():
    tasks = []
    print("!!! Welcome to the To-Do List !!!")
    try:
        num = int(input("Enter the number of tasks you want to add: "))
        for i in range(num):
            task = input(f"Task {i+1}: ")
            tasks.append(task)
    except ValueError:
        print("Please enter a valid number.")
        return

    print("\nYour list was successfully created!")
    
    while True:
        print("\nChoose Operation:")
        print("1. Add\t2. Delete\t3. Update\t4. Delete All\t5. View\t6. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                new_task = input("Enter the new task to add: ")
                tasks.append(new_task)
                print(f"Task '{new_task}' added successfully.")
            
            elif choice == 2:
                if not tasks:
                    print("No tasks to delete.")
                    continue
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")
                idx = int(input("Enter the task number to delete: "))
                if 1 <= idx <= len(tasks):
                    removed = tasks.pop(idx - 1)
                    print(f"Task '{removed}' deleted successfully.")
                else:
                    print("Invalid task number.")
            
            elif choice == 3:
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")
                idx = int(input("Enter the task number to update: "))
                if 1 <= idx <= len(tasks):
                    updated_task = input("Enter the new task: ")
                    tasks[idx - 1] = updated_task
                    print("Task updated successfully.")
                else:
                    print("Invalid task number.")
            
            elif choice == 4:
                tasks.clear()
                print("All tasks deleted successfully.")
            
            elif choice == 5:
                if tasks:
                    print("\nYour To-Do List:")
                    for i, task in enumerate(tasks, 1):
                        print(f"{i}. {task}")
                else:
                    print("List is empty.")
            
            elif choice == 6:
                print("Exiting... Goodbye!")
                break
            else:
                print("Please enter a number between 1 and 6.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")

ToDo_list()
