from lib import storage
from ui import menu, task

from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns

def render():
    render = Panel.fit(
    Columns([
        task.taskTable(storage.getAllTask()), 
        menu.menuTable()], 
        equal=True, expand=True
    ),
    title="Do-It Version 1.0",
    border_style="white",
    title_align="left",
    padding=(1, 2),
    )

    console = Console()
    console.print(render)
    
render()

