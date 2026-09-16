dict1=dict()
for i in range(4):
    admno = int(input("Enter Admission No.: "))
    name = input("Enter Name: ")
    dict1[admno]=name
for i in dict1:
    print("Name and Admission No = ",dict1[i],i)
dict2={5:"Ram", 6:"Piyush", 7:"Lavanya"}
dict1.update(dict2)
print("Updated Dictionary : ")
for i in dict1:
    print("Name and Admission No ",dict1[i],i)
print("Deleting Record (Admission No 1) : ")
if 1 in dict1:
    dict1.pop(1)
else:
    print("Key doesnt exist ")
print(dict1)
print("Deleting Dictionary : ")
del dict1
