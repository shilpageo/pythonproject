#global and local variable

a=2   #global variable
def printa():
    global a
    print(a)
    a=a+2
printa()
print(a)



#stack   operations=push() and pop()
#queue    operations=insert() and del()