from rich.console import Console
from rich.table import Table
from rich import box


def menuTable():
    menu_table = Table(show_header=False, box=box.SQUARE, expand=False, title="Menu~")
    menu_table.add_column("Key", style="cyan", justify="right", width=5)
    menu_table.add_column("Description", style="white")
    menu_table.add_row("[1]", "Add Task")
    menu_table.add_row("[2]", "Edit Task")
    menu_table.add_row("[3]", "Delete Task")
    menu_table.add_row("[F]", "Filter by tags")
    menu_table.add_row("[Q]", "Exit")
    return menu_table
