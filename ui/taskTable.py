from rich.table import Table
from rich import box
from datetime import datetime

def taskTable(tasks=None):
    task_table = Table(box=box.SIMPLE, expand=True, title="Tasks :D") 
    task_table.add_column("Title", justify="left")
    task_table.add_column("Duedate")
    task_table.add_column("Tags")
    task_table.add_column("Time remaining")
    if tasks:
        for task in tasks:
            #format tags
            tag_string = ""
            #print(task["tags"])
            counter = 0 
            for tag in task["tags"]:
                counter += 1
                tag_string += f"#{tag} "
                if counter % 3 == 0:
                    tag_string += "\n"
            #print(tag_string)
            #format duedate
            duedate = ""
            if task["duedate"]:
                duedate = datetime.fromisoformat(task["duedate"]).strftime("%d/%m/%Y")

            #add each task to table
            task_table.add_row(task["title"], duedate, tag_string)
    return task_table