num1=int(input("enter number 1 "))
num2=int(input("enter number 2 "))

print("Arthmetic Operator :: ")
print("+ - * / ** // % ")
print("Addition",num1+num2)
print("Subtraction",num1-num2)
print("Multiplication",num1*num2)
print("Division",num1/num2)
print("Floor Division",num1//num2)
print("Exponent",num1**num2)
print("Remainder",num1%num2)

print("Logical Operator :: ")
print("and or not")
print("and -> 1 == 1 and 1 != 2 answer is",1 == 1 and 1 != 2)
print("and -> 1 == 1 and 1 >= 2 answer is",1 == 1 and 1 >= 2)
print("and -> 1 == 1 or 1 != 2 answer is",1 == 1 and 1 != 2)
print("and -> 1 == 1 or 1 >= 2 answer is",1 == 1 and 1 >= 2)
print("not -> not(1==1)answer is",not(1==1))
print("not -> not(1>1)answer is",not(1>1))

print("Bitwise Operator ::")
print("& | ~ ^ >> <<")
num1=7
num2=4
print("7 & 4 (111 & 100)=",7 & 4)
print("7 | 4 (111 | 100)=",7 | 4)
print("7 ^ 4 (111 ^ 100)=",7 ^ 4)
print("~10(~1001)=",~10)
print("10 >> 1",10 >> 1)
print("10 << 1",10 << 1)

print("Identity Operators")
print("is,not is")
a=10
b=10
c=a
print(a is b)
print(a is c)
print(a == b)
print(a == c)
   
