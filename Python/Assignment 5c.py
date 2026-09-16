mytuple = (42, 17, 89, 2, 55, 10, 104)
minval = mytuple[0]
maxval = mytuple[0]
for num in mytuple:
    if num < minval:
        minval = num
    if num > maxval:
        maxval = num
print("The tuple is:",{mytuple})
print("The minimum number is:",{minval})
print("The maximum number is:",{maxval})


#mytuple = (42, 17, 89, 2, 55, 10, 104)
#minval = min(mytuple)
#maxval = max(mytuple)
#print("The tuple is:",{mytuple})
#print("The minimum number is:",{minval})
#print("The maximum number is:",{maxval})
