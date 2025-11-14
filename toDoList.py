toDo = ['study', 'mopping', 'cleaning', 'washing']
while True:
    print("1. Add")
    print("2. Delete")
    print("3. only view")
    print("4. Exit")

    choice = int(input("Enter the number: "))

    if choice == 1:
        task = input("Enter the task")
        toDo.append(task)
        print("Your updated To Do List is:", toDo)

    elif choice == 2:
        if not toDo:
            print("Your To Do List is empty")
        else:
            print("Your To Do List:", toDo)
            task = input("Enter task name to delete")
            if task in toDo:
                toDo.remove(task)
                print("Your task", task , "has been deleted and your new To Do List is", toDo)

    elif choice == 3:
        if not toDo:
            print("Your To Do List is Empty")
        else:
            print("Your To Do List is:")
            for i in toDo:
                print(i)

    elif choice == 4:
        print("Exiting. Thank you")
        break

    else:
        print("Enter the correct number between 1-4")