print("โปรแกรมจัดการงาน")
print("1. เพิ่มงาน")
print("2. แสดงงานทั้งหมด")
print("Q: ออกจากโปรแกรม")
work_list = []

choice = input("เลือกเมนู: ")
if choice == "1":
    input_work = input("เพิ่มงาน: ")
    work_list.append(input_work)
    print("เพิ่มงานสำเร็จ กด Enter เพื่อกลับสู่เมนูหลัก")
elif choice == "2":
    for i in work_list:
        print(i)
elif choice == "Q":
    print("ออกจากโปรแกรม")
