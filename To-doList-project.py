def display_tasks(task_list):
    print("To-Do List:")
    for index, task in enumerate(task_list):
        print(f"{index + 1}. {task}")

def main():
    tasks = []

    while True:
        print("\nMenu:")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Mark task as completed")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            new_task = input("Enter the new task: ")
            tasks.append(new_task)
            print("Task added!")
        elif choice == "3":
            display_tasks(tasks)
            task_index = int(input("Enter the index of the completed task: ")) - 1
            if 0 <= task_index < len(tasks):
                completed_task = tasks.pop(task_index)
                print(f"Task '{completed_task}' marked as completed!")
            else:
                print("Invalid index.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
