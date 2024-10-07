import add 
import remove 
import view
#I assigned an empty list to a variable called taskApp
taskApp =[ ]
#This is the menu function where you get to choose an option you like.
def menu():
    while True:
        print("\nTo-do list menu")
        print("1. Add Tasks")
        print("2. Remove Tasks")
        print("3. View Task")
        print("4. Exit")         
        choice = input("Enter your choice :")
        if choice == '1':        
            while True:
                task = input("Enter the task (or type 'done' to finish) ")
                if task.lower()=='done':
                    break
                add(task)
        elif choice == '2':
            taskToBeRemoved = input("Enter the task you want to remove: ")
            remove(taskToBeRemoved)
        elif choice == '3':
                view(task)
        elif choice == '4':
            print("Good bye!")
            break
        else:
            print("invaild choice. please choice again!")
menu()