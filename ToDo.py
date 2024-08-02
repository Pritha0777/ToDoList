#Code to create a simple To-Do List 

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
       # display()
       pass
    elif action == "2":
        task = input("Enter the task: ")
       # add_task(task)
    elif action == "3":
        try:
            #display()
            task_num = int(input("Enter task number that needs to be marked as completed"))
            #completed(task_num)
        except ValueError:
            print("Invalid input, enter a NUMBER")
    elif action == "4":
        try:
            #display()
            task_num = int(input("Enter the task number that needs to be removed"))
           # removed(task_num)
        except ValueError:
            print("Invalid input, enter a NUMBER")
    elif action == "5":
        break
    else:
        print("Enter a valicd choice of action")