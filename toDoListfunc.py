toDo = ['study', 'mopping', 'cleaning', 'washing']

def show_menu():
    print("1. Add")
    print("2. Delete")
    print("3. only view")
    print("4. Exit")


def add_task():
    task = input("Enter the task")
    toDo.append(task)
    print("Your updated To Do List is:", toDo)

def delete_task():
    if not toDo:
        print("Your To Do List is empty")
    else:
        print("Your To Do List:", toDo)
        task = input("Enter task name to delete")
        if task in toDo:
            toDo.remove(task)
            print("Your task", task , "has been deleted and your new To Do List is", toDo)
        else:
            print("Task Not Found")

def view_task():
    if not toDo:
        print("Your To Do List is Empty")
    else:
        print("Your To Do List is:")
        for i in toDo:
            print(i)

while True:
    show menu()
    choice = input("Enter the number")
    
    if choice == 1:
        add_task()
    elif choice == 2:
        delete_task()
    elif choice == 3:
        view_task()
    elif choice == 4:
        print("Exiting. Thank you")
        break
    else:
        print("Invalid input, please enter the correct number between 1-4")