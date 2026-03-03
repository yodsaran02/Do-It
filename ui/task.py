from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

console = Console()

def taskTable(tasks=None):
    task_table = Table(box=box.SIMPLE, expand=True) 
    task_table.add_column("Title", justify="left")
    task_table.add_column("Duedate")
    task_table.add_column("Duedate")
    return task_table