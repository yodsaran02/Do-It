from lib import storage
from ui import menuTable, taskTable
from datetime import datetime

from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich.prompt import Prompt
console = Console(color_system="auto")

def render(tasks=None):
    if not tasks:
        tasks = storage.getAllTask()
    render = Panel.fit(
    Columns([
        taskTable.taskTable(tasks), 
        menuTable.menuTable()], 
        equal=True, expand=True
    ),
    title="Do-It Version 1.0",
    border_style="white",
    title_align="left",
    padding=(1, 2),
    )
    console.print(render)

render()
while True:
    choice = Prompt.ask("Select a menu")
    if choice == "1":
        input_task = Prompt.ask("Title")
        if input_task not in storage.getAllTaskName():
            raw_deadline = Prompt.ask("Deadline (DD/MM/YY)")
            deadline = datetime.strptime(raw_deadline, "%d/%m/%y") if raw_deadline else None
            storage.createTask(input_task, deadline)
        else:
            render()
            console.print("Task already existed!", style="white on red")
            continue
    elif choice == "2":
        input_task = Prompt.ask("Title")
        task = storage.getTask(input_task)
        if task:
            task_hash = task["hash"]
            new_title = Prompt.ask("New Title", default=None)
            new_duedate = Prompt.ask("New Deadline (DD/MM/YY)", default=None)
            new_is_done = Prompt.ask("Is Done? (y/n)", default=None)
            added_tags = Prompt.ask("Added Tags (space separated)", default=None)
            removed_tags = Prompt.ask("Removed Tags (space separated)", default=None)
            if new_title:
                task["title"] = new_title
            if new_duedate:
                task["duedate"] = storage.parseDueDate(datetime.strptime(new_duedate, "%d/%m/%y"))
            if new_is_done:
                task["isDone"] = True if new_is_done == "y" else False
            if added_tags:
                #print(added_tags)
                task["tags"].extend(added_tags.replace("#","").split())
                #print(task["tags"])
            if removed_tags:
                for tag in removed_tags.replace("#","").split():
                    task["tags"].remove(tag)
            storage.editTask(task)
        else:
            render()
            console.print("No task found!", style="white on red")
            continue
    elif choice == "3":
        input_task = Prompt.ask("Title")
        task = storage.getTask(input_task)
        if task:
            storage.deleteTask(task["hash"])
        else:
            render()
            console.print("No task found!", style="white on red")
            continue
    elif choice == "f" or choice == "F":
        print("All Tags: ", end="")
        for tag in storage.getAllTags():
            print(f"#{tag}", end=" ")
        print()
        input_tags = Prompt.ask("Tags (space separated)")
        tags = input_tags.replace("#","").split()
        tasks = storage.getAllTask()
        if tags:
            filtered_tasks = [task for task in tasks if all(tag in task["tags"] for tag in tags)]
            render(tasks=filtered_tasks)
            continue
        else:
            render()
            console.print("No tags!", style="white on red")
            continue
    elif choice == "q" or choice == "Q":
        print()
        break
    render()

