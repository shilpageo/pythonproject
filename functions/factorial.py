#method1

def fact():
    num=int(input("enter number"))
    fact=1
    for i in range(1,num+1):
     fact*=i
    print(fact)
fact()

#method2

def fact(n1):
    fact=1
    for i in range(1,n1+1):
        fact*=i
    print(fact)
fact(5)

#method3

def fact(num1):
    fact=1
    for i in range(1,num1+1):
        fact*=i
    return fact
d=fact(5)
print(d)
