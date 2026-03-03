from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
from datetime import datetime
console = Console()

def taskTable(tasks=None):
    task_table = Table(box=box.SIMPLE, expand=True) 
    task_table.add_column("Title", justify="left")
    task_table.add_column("Duedate")
    task_table.add_column("Tags")
    task_table.add_column("Time elapsed")
    if tasks:
        for task in tasks:
            #format tags
            tag_string = ""
            for tag in task["tags"]:
                tag_string += f"#{tag} "

            #format duedate
            duedate = datetime.fromisoformat(task["duedate"]).strftime("%d/%m/%Y")

            #add each task to table
            task_table.add_row(task["title"], duedate, tag_string, str(task["actual_time"]))
    return task_table