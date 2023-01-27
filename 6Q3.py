
from math import factorial
n=int(input("enter the no of rows you want"))
for i in range(n):
    for a in range(n-i+1):
        print(end="  ")
    for a in range(i+1):
        print(factorial(i)//(factorial(a)*factorial(i-a)),end="   ")

    print()        