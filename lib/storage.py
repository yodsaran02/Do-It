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
        duedate = duedate.isoformat()
    return duedate

def createTask(title, duedate=None): 
    tasks = getAllTask()
    duedate = parseDueDate(duedate)
    currentTask = {
        "hash": uuid.uuid4().hex,
        "title": title,
        "duedate": duedate,
        "isDone": False,
        "tags": [],
    }
    tasks.append(currentTask)
    writeToJson(tasks)

def deleteTask(taskHash):
    tasks = getAllTask()
    for task in tasks:
        if task["hash"] == taskHash:
            tasks.remove(task)
    writeToJson(tasks)
    

def editTask(newTask):
    tasks = getAllTask()
    for task in tasks:
        if task["hash"] == newTask["hash"]:
            task["title"] = newTask["title"]
            task["duedate"] = newTask["duedate"]
            task["tags"] = newTask["tags"]
            task["isDone"] = newTask["isDone"]
        else:
            return "Not found"
    writeToJson(tasks)
            
def getAllTaskName():
    tasks = getAllTask()
    return [task["title"] for task in tasks]

def getTask(title):
    tasks = getAllTask()
    for task in tasks:
        if task["title"] == title:
            return task
    return None
    
def getAllTaskName():
    tasks = getAllTask()
    tasksName = [task["title"] for task in tasks]
    return tasksName
    
def getAllTags():
    tasks = getAllTask()
    tags = []
    for task in tasks:
        for tag in task["tags"]:
            if tag not in tags:
                tags.append(tag)
    return tags


