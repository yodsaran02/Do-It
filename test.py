from datetime import datetime
from lib import storage


print("Do-It Version 1.0")
print("Select Menu below")
print("1. add work")
print("2. edit work")
print("3. show all work")
print("4. mark work as done")
print("Q: save&exit")

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
        storage.createTask(input_work, duedate)
        print("successfully added", end="\n\n")
    elif choice == "3":
        work_list = storage.getAllTask()
        for i in work_list:
            print(i["title"], end="")
            if i["duedate"] is not None:
                print(" (Due: {})".format(i["duedate"].strftime("%d/%m/%Y")),)
            else:
                print(" (No due date)")
        print()
    elif choice == "4":
        input_work = input("Input finished work: ")
        found = False
        if not found:
            print("work not found", end="\n\n")
    else: print("Invalid menu, please select again")
