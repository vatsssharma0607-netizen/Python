side = float(input("Enter the length of ONE side of the square: "))
if side <= 0:
    print("A side length must be a positive number.")
else:
    area = side * side 
    perimeter = 4 * side 
    print("The side length you entered was: ",{side})
    print("The Area of the square is: ",{area})
    print("The Perimeter of the square is: ",{perimeter})
