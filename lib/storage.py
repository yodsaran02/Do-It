import json
import uuid 

def getAllTask():
    with open("task.json", mode="r", encoding="utf-8") as read_file:
        tasks = json.load(read_file)
    return tasks

def writeToJson(data):
    with open("task.json", mode="w", encoding="utf-8") as read_file:
        json.dump(data, read_file)

def parseDueDate(duedate):
    if duedate:
        duedate = duedate.toISOString()
    return duedate

def createTask(title, duedate=None): 
    tasks = getAllTask()
    duedate = parseDueDate(duedate)
    currentTask = {
        "hash": uuid.uuid4().hex
        "title": title,
        "duedate": duedate,
        "tags": [],
        "actual_time": 0,
        "predicted_time": None
    }
    tasks.append(currentTask)
    writeToJson(tasks)

def editTask(hash, title=None, duedate=None, actual_time=0, predicted_time=None, tags=[]):
    tasks = getAllTask()
    for task in tasks:
        if task["hash"] == hash:
            task["title"] = title
            task["duedate"] = parseDueDate(duedate)
            task["actual_time"] = actual_time
            task["predicted_time"] = predicted_time
            task["tags"] = tags
        else:
            return "Not found"
            
def getAllTaskName():
    tasks = getAllTask()
    return [task["title"] for task in tasks]

def getTask(title):
    tasks = getAllTask()
    for task in tasks:
        if task["title"] == title:
            return task
    return None
    
    




