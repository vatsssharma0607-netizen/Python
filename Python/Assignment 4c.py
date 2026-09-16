List1=[1,3,6,9]
List2=[1,6,10,2]
List3=[]
for i in List1:
    if i in List2:
        List3.append(i)
print("Common Items are ",List3)
