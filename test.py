print("Do-It Version 1.0")
print("Select Menu below")
print("1. add work")
print("2. show work")
print("Q: exit")
work_list = []

while True:
    choice = input("Select Menu: ")
    if choice == "Q" or choice == "q":
        print("Program is exiting...")
        break
    if choice == "1":
        input_work = input("Tittle: ")
        work_list.append(input_work)
        print("successfully added", end="\n\n")
    elif choice == "2":
        for i in work_list:
            print(i)
    else: print("Invalid menu, please select again")
