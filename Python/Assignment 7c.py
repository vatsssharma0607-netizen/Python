userinput = input("Enter numbers separated by spaces: ")
numbersSet = {int(n) for n in userinput.split()}
print("Set after input:",numbersSet)
rem = int(input("Enter number to remove: "))
numbersSet.discard(rem) 
print("Final set:",numbersSet)
