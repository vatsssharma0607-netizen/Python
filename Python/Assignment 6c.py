dict1={"item1":"Apple","item2":"Banana","item3":"Apple","item4":"Orange","item5":"Banana"}
uniquelist = []
for value in dict1.values():
    if value not in uniquelist:
        uniquelist.append(value)
print("Original Dictionary:", dict1)
print("Unique Values:", uniquelist)







#dict1={"item1":"Apple","item2":"Banana","item3":"Apple","item4":"Orange","item5":"Banana"}
#uniquevalues = set(dict1.values())
#print("Original Dictionary:",dict1)
#print("Unique Values:", list(uniquevalues))
