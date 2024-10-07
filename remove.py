#To remove task in the to-do list i need to create a function for that
def remove_task(taskToBeRemoved):
    global taskApp
    inital_length = len(taskApp)
    #I called this particular part of my code list comprehension...
    # What does that mean? It means to create a new list that include only the tasks that are not equal to taskToBeRemoved.
    taskApp =[task for task in taskApp if task != taskToBeRemoved]
    if len(taskApp) < inital_length:
        print(f"Task '{taskToBeRemoved}' removed")
    else:
        print(f"Task '{taskToBeRemoved}' not found")
        