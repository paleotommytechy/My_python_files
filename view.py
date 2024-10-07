#Add some conditional statement in the view task function block to detect empty list and if any task is added then list them out
#I used enumerate function for numbering each task added.
def view_task(task):
    if not task:
        print("No task avaliable!.")
    else:
        for index, task in enumerate(taskApp, 1):
            print(f"{index}. {task}")