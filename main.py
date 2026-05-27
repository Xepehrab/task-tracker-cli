import sys
import json 
import os 
from datetime import datetime

#Task File name 
FILE_NAME="task.json"   

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return[]
    try:
        with open(FILE_NAME,'r',encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []
    
def save_tasks(tasks):
    with open(FILE_NAME,'w',encoding='utf-8') as file:
        json.dump(tasks,file,indent=4)


def add_task(description):
    """add new task"""
    tasks=load_tasks()

    task_id=max(task['id'] for task in tasks)+1 if tasks else 1

    current_time=datetime.now().isoformat()
  
    task_dict={
        'id':task_id,
        'description':description,
        'status':'todo',
        'createdAt': current_time,
        'updatedAt' : current_time
    }
    tasks.append(task_dict)
    save_tasks(tasks)
    print(f"Task  {description} added Successfully (ID : {task_id})")

def update_task(task_id,new_description):
    """update a task description"""
    tasks=load_tasks()
    for task in tasks:
        if task['id']== task_id:
            current_time= datetime.now().isoformat()
            task['description']= new_description
            task['updatedAt']= current_time
            save_tasks(tasks)
            print(f" Task {task_id} updated successfully")
            return
    print(f'task with ID {task_id} not found')

def delete_task(task_id):
    tasks=load_tasks()
    for task in tasks:
        if task['id']== task_id:
            tasks.remove(task)
            print(f'task {task_id} removed Successfully')
            save_tasks(tasks)
            return
    print(f"Cant find task {task_id} ")


def change_status(new_status,task_id):
    tasks=load_tasks()
    for task in tasks:
        if task['id']== task_id:
            current_time= datetime.now().isoformat()
            task['status']= new_status
            task['updatedAt']=current_time
            save_tasks(tasks)
            print(f'task {task_id} status updated successfully')
            return
    print(f"Cant find task {task_id} ")

def list_tasks(status_filter=None):
    tasks=load_tasks()
    if not tasks:
        print('No task Found :( . Add one and try again :) ')
        return
    for task in tasks:
        if status_filter is None or task['status']== status_filter:
            print(f'ID: {task['id']} |'
                  f"Status: [{task['status']}] |"
                  f'{task['description']}'
                  )
            found=True
        if not found:
            print(f'No task with status {status_filter} found')
    print("-------------------\n")
        
            
def main():
    #If user enter any command 
    if len(sys.argv)<2:
        print('Usage python task_cli.py <command> [arguments]')
        return
    #Get main Command
    command=sys.argv[1]

    if command=='add':
        if len(sys.argv)<3:
            print("Error: please provide a task description")
        else:
            add_task(sys.argv[2])
    elif command=='update':
        if len(sys.argv)<4:
            print("Erro please enter task id and description")
        else:
            update_task(sys.argv[2],sys.argv[3])
    elif command=='delete':
        if len(sys.argv)<3:
            print('"Error: please provide a task ID')
        else:
            delete_task(int(sys.argv[2]))
    elif command== ' in-progress':
        if len(sys.argv)<3:
            print('"Error: please provide a task ID')
        else:
            change_status("in-progress",int(sys.argv[2]))
    elif command== ' done':
        if len(sys.argv)<3:
            print('"Error: please provide a task ID')
        else:
            change_status("done",int(sys.argv[2]))
    elif command =='list':
        if len(sys.argv)==3:
            list_tasks(sys.argv[2])
        else:
            list_tasks()
    else:
        print(f'Unknow command {command}')
if __name__=="__main__":
    main()

