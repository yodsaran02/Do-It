from ui.tasklist import TableApp
from lib import storage

tasks = storage.getAllTask()
ROWS = [("Title", "Duedate", "Done?", "Tags", "time elapsed")]
for task in tasks:
    task_tuple = (task["title"], task["duedate"], task["isDone"], task["tags"], task["actual_time"])
    ROWS.append(task_tuple)

app = TableApp(rows=ROWS)
if __name__ == "__main__":
    app.run()