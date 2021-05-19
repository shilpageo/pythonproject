lst=[]
num=int(input("enter the size"))
op=int(input("enter th operation","\n","1.push,2.pop")
siz=0
n=0

def push():
    global num,siz
    if siz>=num:
        print("queue is full")
    else:
        p=int(input("enter the element"))
        lst.append(p)
        siz+=1
        print(lst)
def pop():
    global num,siz
    if siz<=0:
        print("queue is empty")
    else:
        lst.pop(0)
        siz+=1
        print(lst)
while n!=1:
    print("enter the operation")
    opt = int(input("1:push,2:pop"))
    if opt == 1:
        push()
    else:
        pop()





