import json

def getAllTask():
    with open("task.json", mode="r", encoding="utf-8") as read_file:
        tasks = json.load(read_file)
    return tasks

def createTask(name, deadline=None): 
    tasks = getAllTask()
    



