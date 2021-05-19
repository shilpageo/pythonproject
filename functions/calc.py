num1=float(input("enter number"))
num2=float(input("enter a number"))
op=input("enter operator")
def add(num1,num2):
    s=num1+num2
    print(s)
def sub(num1,num2):
    s=num1+num2
    print(s)
def mul(num1,num2):
    m=num1+num2
    print(m)
def div(num1,num2):
    d=num1+num2
    print(d)
if(op=='+'):
    add(num1,num2)
elif(op=='-'):
    sub(num1,num2)
elif(op=='*'):
    mul(num1,num2)
elif(op=='/'):
    div(num1,num2)
else:
    print("enter valid operator")
