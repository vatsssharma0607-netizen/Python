def addAssignment():
    file = open("assignment.txt","a")
    name = input("Enter Assignment name ")
    subject = input("Enter Assignment subject ")
    date = input("Enter Assignment date ")
    str1 = f"'Pending' - {name}, {subject}, {date}\n"
    file.write(str1)
    file.close()
def displayAssignment():
    file = open("assignment.txt","r")
    L1 = file.readlines()
    if L1 ==[]:
        print("NO Assignment ADDED")
        return
    for i in L1:
        L2 = i.split("-")
        if L2[0].strip() =="'Pending'":
            print("⌛",L2[0],L2[1])
        else:
            print("✔️",L2[0],L2[1])
def markasDone():
    file = open("assignment.txt","r")
    L1 = file.readlines()
    if L1 ==[]:
        print("NO Assignment ADDED")
        return
    count = 1
    for i in L1:
        L2 = i.split("-")
        if L2[0].strip() =="'Pending'":
            print(count , "- ⌛",L2[0],L2[1])
            count+=1
    option  = int(input("Enter task number "))
    file.close()
    if (option > count):
        print("Invalid Number Entered ")
        return
    else:
        task_text = L1[option - 1].replace("'Pending'", "").strip()
        L1[option - 1] = f"'Done' {task_text}"
        file = open("assignment.txt","w")
        file.writelines(L1)
        file.close()
        print("Assignment Status Updated ")
        
def searchAssignment():
    print("-- Search Menu -- ")
    print("Enter Assignment Keyword (name, subject, date  etc ")
    key = input("")
    file = open("assignment.txt","r")
    L1 = file.readlines()
    if L1 ==[]:
        print("NO Assignment ADDED")
        return
    else:
        for i in L1:
            if key.lower() in i.lower():
                print(i)
    
def deleteAssignment():
    print("Enter Assignment Keyword (name, subject, date  etc ")
    key = input("")
    file = open("assignment.txt","r")
    L1 = file.readlines()
    if L1 ==[]:
        print("NO Assignment ADDED")
        return
    else:
        count = 0
        print("Assignments :: ")
        print("----------------------")
        for i in L1:
            if key.lower() in i.lower():
                count += 1 
                print(count, i)
        print("----------------------")
        print("Enter number you want to delete : ")
        option = int(input(" "))
        if option > count :
            print("Invalid Number ")
        else:
            L1.pop(option -1 )
            file = open("assignment.txt","w")
            file.writelines(L1)
            file.close()
            print("Assignment Deleted ")
            
while True:
    print("\n\n-- Main Menu -- ")
    print("\n1. Add Assignment")
    print("2. Display Assignments")
    print("3. Mark as Done ")
    print("4. Search Assignment")
    print("5. Delete Assignment")
    print("0. Exit")
    try:
        choice = int(input("enter option "))
    except:
        print("Invalid Data type entered ")
        continue
    if choice  == 1 :
        addAssignment()
    elif choice == 2:
        displayAssignment()
    elif choice == 3:
        markasDone()
    elif choice == 4:
        searchAssignment()
    elif choice == 5:
        deleteAssignment()
    elif choice == 0:
        break
    else:
        pass
