from datetime import datetime
from lib import storage


print("Do-It Version 1.0")
print("Select Menu below")
print("1. add work")
print("2. show work")
print("3. finished work")
print("Q: save&exit")
work_list = storage.getAllTask()

while True:
    choice = input("Select Menu: ")
    if choice == "Q" or choice == "q":
        print("Program is exiting...")
        break
    if choice == "1":
        input_work = input("Tittle: ")
        while True:
            raw_deadline = input("Duedate (DD/MM/YY), leave blank if no due date: ")
            if raw_deadline == "":
                duedate = None
                break
            try:
                duedate = datetime.strptime(raw_deadline, "%d/%m/%y")
                break
            except ValueError:
                print("Invalid date format. Please enter the date in DD/MM/YY format.")
        work_list.append({"title": input_work, "duedate": duedate})
        work_list.sort(key=lambda x: (x["duedate"] is None, x["duedate"]))
        print("successfully added", end="\n\n")
    elif choice == "2":
        for i in work_list:
            print(i["title"], end="")
            if i["duedate"] is not None:
                print(" (Due: {})".format(i["duedate"].strftime("%d/%m/%Y")),)
            else:
                print(" (No due date)")
        print()
    elif choice == "3":
        input_work = input("Input finished work: ")
        found = False
        for i in work_list:
            if i["title"] == input_work:
                work_list.remove(i)
                print("successfully removed", end="\n\n")
                found = True
                break
        if not found:
            print("work not found", end="\n\n")
    else: print("Invalid menu, please select again")
