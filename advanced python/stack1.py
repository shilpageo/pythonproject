lst=[]
num=int(input("enter the size"))
op=int(input("enter the operation", "\n","1. push 2.pop"))
n=0
siz=0
def push():
    global num,siz
    if siz>=num:
        print("stack is full")
    else:
       p=int(input("enter the element"))
       lst.append(p)
       siz+=1
       print(lst)
def pop():
   global num,siz
   if siz<=0:
     print("stack is empty")
   else:
       lst.pop(0)
       siz-=1
       print(lst)
while n!=1:
    print("enter the operation")
    opt=int(input("1:push,2:pop"))
    if opt==1:
        push()
    else:
        pop()







