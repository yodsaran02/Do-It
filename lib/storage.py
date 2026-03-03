import json
import uuid 

def getAllTask():
    with open("task.json", mode="r", encoding="utf-8") as read_file:
        tasks = json.load(read_file)
    return tasks

def writeToJson(data):
    with open("task.json", mode="w", encoding="utf-8") as write_file:
        json.dump(data, write_file)
    return None

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
            print(task["duedate"])
            task["tags"] = newTask["tags"]
            task["isDone"] = newTask["isDone"]
    print(tasks)
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
    
def getAllTags():
    tasks = getAllTask()
    tags = []
    for task in tasks:
        for tag in task["tags"]:
            if tag not in tags:
                tags.append(tag)
    return tags


