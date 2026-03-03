from textual.app import App, ComposeResult
from textual.widgets import DataTable

class TableApp(App):
    def __init__(self, rows):
        super().__init__()
        self.rows = rows

    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*self.rows[0])
        table.add_rows(self.rows[1:])