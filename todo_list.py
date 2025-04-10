tasks=[]
while True:
    print("""
    Todo List Menu:
    1.Add a task
    2.View Task
    3.Remove a task
    4.Exit     
    """)
    user_choice=int(input("Enter your choice. "))
    if user_choice==1:
        task=input("Enter the task you want to add: ")
        tasks.append(task)
        print("task added successfully.")
        
    elif user_choice==2:
        if not tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
        
    elif user_choice==3:
        task=input("Enter the task you want to remove: ")
        if task in tasks:
            tasks.remove(task)
            print("task removed successfully.")
        else:
            print("task not found.")
        
    elif user_choice==4:
        print("Goodbye.")
        break
    else:
        print("Invalid Number.")
        break
