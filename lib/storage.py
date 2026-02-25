import json

def getAllTask():
    with open("task.json", mode="r", encoding="utf-8") as read_file:
        tasks = json.load(read_file)
    return tasks

def writeToJson(data):
    with open("task.json", mode="w", encoding="utf-8") as read_file:
        json.dump(data, read_file)

def createTask(title, duedate=None): 
    tasks = getAllTask()
    if duedate:
        duedate = duedate.toISOString()
    currentTask = {
        "title": title,
        "duedate": duedate,
        "tags": [],
        "actual_time": 0,
        "predicted_time": None
    }
    tasks.append(currentTask)
    writeToJson(tasks)

def editTask(title):
    tasks = getAllTask()

def getAllTaskName():
    tasks = getAllTask()
    return [task["title"] for task in tasks]

def getTask(title):
    tasks = getAllTask()
    for task in tasks:
        if task["title"] == title:
            return task
    return None
    
    




