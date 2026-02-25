print("Do-It Version 1.0")
print("Select Menu below")
print("1. add work")
print("2. show work")
print("3. remove finished work")
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
    elif choice == "3":
        input_work = input("Input finished work: ")
        if input_work in work_list:
            work_list.remove(input_work)
            print("successfully removed", end="\n\n")
        else:
            print("work not found", end="\n\n")
    else: print("Invalid menu, please select again")
