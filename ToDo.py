#Code to create a simple To-Do List 
tasks = []
#Displaying the list
def display():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i}. {task['task']} ({status})")

#Adding a task
def add_task(task_name):
    task = {"task": task_name, "completed": False}
    tasks.append(task)
    print(f"Task '{task_name}' added to your to-do list.")
    display()

#Marking the task complete
def completed(task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number. Please enter a valid task number.")
    display()

#Removing the task
def removed(task_number):
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['task']}' removed from your to-do list.")
    else:
        print("Invalid task number. Please enter a valid task number.")
    display()

#Main function
while True:
    print("\nOptions")
    print("Display the list")
    print("Add a new task")
    print("Mark a task as completed")
    print("Remove a task")
    print("Exit")
    action = input("Enter the choice of action: ")
    if action == "1":
       display()
    elif action == "2":
        task = input("Enter the task: ")
        add_task(task)
    elif action == "3":
        try:
            display()
            task_num = int(input("Enter task number that needs to be marked as completed: "))
            completed(task_num)
        except ValueError:
            print("Invalid input, enter a NUMBER")
    elif action == "4":
        try:
            display()
            task_num = int(input("Enter the task number that needs to be removed: "))
            removed(task_num)
        except ValueError:
            print("Invalid input, enter a NUMBER")
    elif action == "5":
        break
    else:
        print("Enter a valicd choice of action")