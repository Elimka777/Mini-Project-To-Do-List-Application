tasks = []
def addTask():
    print()
    num_tasks = int(input("Number of tasks you want to add: "))
    for i in range(num_tasks):
        task=input(f"Enter the {i + 1} task:")
        tasks.append({"task": task, "complete": False})
        print("Task added.")
def listTask():
    print("\nTasks:")
    for index, task in enumerate(tasks):
        status = "complete" if task["complete"] else "incomplete"
        print(f"{index+1}. {task['task']} - {status}")
def markTask():
    try:  
     task_index = int(input("Enter the number of the task to mark as done:")) - 1
     if 0 <= task_index< len(tasks):
        tasks[task_index]["complete"] = True
        print(f"Task {tasks[task_index]['task']} marked as complete")
     else:
        print('Invalid task number. Please try again.')
    except ValueError:
        print("Please enter a number.")
    
def deleteTask():
    try: 
     task_index = int(input("Enter the number of the task you want to delete: ")) - 1
     if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task['task']}' removed.")
     else:
        print('Invalid task number. PLease try again.')
    except ValueError:
        print("Please enter a number.")


if __name__ == "__main__":
    #Let's create a loop to run the app
    print("welcome to the to_do list app✍️. Time for productivity!")
    while True: 
        print("\nMenu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Quit")
        print("\n...")
        choice = input("Enter your choice: ")
        if choice == "1":
            addTask()
        elif (choice == "2"):
            listTask()
        elif (choice == "3"):
            markTask()
        elif (choice == "4"):
            deleteTask()
        elif (choice == "5"):
            break
        else:
            print("Invalid input. Please try again.")
    print("Goodbye!👋")