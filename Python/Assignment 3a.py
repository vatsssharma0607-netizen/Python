n = int(input("Enter a number: "))
copy = n  
rev = 0
if n < 0:
    num = abs(n)
else:
    num = n
while num > 0:
    digit = num % 10    
    rev = rev * 10 + digit 
    num = num // 10       
if copy < 0:
    rev = -rev
print("The reversed number is:", rev)
