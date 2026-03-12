# to do list program but it saves user task in the text file
from pathlib import Path

file_path = "tasks-to-do.txt"
task_file = Path(file_path)

if not task_file.exists():
    task_file.touch()
tasks = []
with open(file_path) as importing_tasks:
    tasks = [ task.strip() for task in importing_tasks.readlines()]


while True:
    menu = input("Press 1 to Add a task, 2 to View tasks, 3 to Delete a task, or 'q' to Quit. : ")
    if menu == '1':
        task = input("Enter the task : ")
        tasks.append(task)
    elif menu == '2':
        if len(tasks) == 0:
            print("The list is empty!")
        else:
            for index, task  in enumerate(tasks , start= 1):
                print(f'{index}. {task}')
    elif menu == '3':
        try:
            delete = int(input("Enter which task do you want to delete (task number): "))
            if 1 <= delete <= len(tasks):
                print(f'{tasks[delete - 1]} has been deleted from the tasks')
                del tasks[delete - 1]
            else:
                print("The Task Number doesn't exist")
        except ValueError as e:
            print(f'Error: {e}')
    elif menu.lower() == 'q':
        with open(file_path , 'w') as f:
            for task in tasks:
                f.write(f'{task}\n')
        break
    else:
        print("Invalid input")