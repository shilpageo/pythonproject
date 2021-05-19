#index error

lst=[1,2,3,4,5]
a=int(input("enter index"))

try:
    print(lst[a])

except:
    print("index error occured")
