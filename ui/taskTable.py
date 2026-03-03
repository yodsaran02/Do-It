from rich.table import Table
from rich import box
from datetime import datetime

def taskTable(tasks=None):
    task_table = Table(box=box.SIMPLE, expand=True, title="Tasks :D") 
    task_table.add_column("Title", justify="left")
    task_table.add_column("Done")
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
            print(tag_string)
            #format duedate
            duedate = ""
            if task["duedate"]:
                duedate = datetime.fromisoformat(task["duedate"]).strftime("%d/%m/%Y")

            isDone = "✓" if task["isDone"] else "x"
            #add each task to table
            time_remaining = ""
            if task["duedate"]:
                time_remaining = datetime.fromisoformat(task["duedate"]) - datetime.now()
                if time_remaining.total_seconds() < 0:
                    time_remaining = "Missing"
                elif time_remaining.total_seconds() >= 86400:
                    time_remaining = f"{int(time_remaining.total_seconds() // 86400)}d"
                time_remaining = str(time_remaining).split(".")[0] #remove microseconds

            task_table.add_row(task["title"], isDone, duedate, tag_string, time_remaining)
    return task_table