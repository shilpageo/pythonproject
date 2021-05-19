#method1
def sub():
    num1=int(input("enter a number1"))
    num2=int(input("enter a number2"))
    sub=num1-num2
    print(sub)
sub()

#method2

def sub(n1,n2):
    res=n1-n2
    print(res)
sub(20,10)

#method3

def sub(num1,num2):
    res=num1-num2
    return res
d=sub(10,20)
print(d)
