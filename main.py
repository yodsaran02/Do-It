from datetime import datetime
from lib import storage
from ui import menu, task

from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns

panel = Panel.fit(
    Columns([task.taskTable(), menu.menuTable()]),
    title="My Panel",
    border_style="red",
    title_align="left",
    padding=(1, 2),
)

console = Console()
console.print(panel)