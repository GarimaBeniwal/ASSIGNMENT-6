def is_perfect():
    num=int(input("enter a number:"))
    divisors=[i for i in range(1,num) if num%i==0]
    if sum(divisors)==num:
        print(num,"is a perfect no")
    else:
        print(num,"is not a perfect no")

is_perfect()        
 

