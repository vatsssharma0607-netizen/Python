set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Set A:",set1)
print("Set B:",set2)
unionSet = set1 | set2  
print("Union:",unionSet)
intersectionSet = set1 & set2  
print("Intersection:",intersectionSet)
differenceSet = set1 - set2  
print("Difference (A - B):",differenceSet)
symdiffSet = set1 ^ set2  
print("Symmetric Difference:",symdiffSet)
set1.clear()
print("Set A after clearing:",set1)
