n=3
k=1
for i in range (n):
    print(" "*(n-i),end="")
    print("*"*k)
    k=k+2
k=k-4
for i in range(n-1):
    print(" "*(i+2),end="")
    print("*"*k);
    k=k-2
