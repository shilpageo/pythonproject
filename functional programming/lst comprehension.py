lst=[2,3,4,5,6]
#find squares

squares=[num**2 for num in lst]
print(squares)

fruits=["apple","orange","mango"]

pairs=[(fruit,fruit)for fruit in fruits]
print(pairs)

lst1=[10,20]
lst2=[30,40]
#(10,30),(10,40),(20,30),(20,40)

pairs_lst=[(num1,num2) for num1 in lst1 for num2 in lst2]
print(pairs_lst)

lst1=[1,2,3,4,5]
evens=[num for num in lst1 if num%2==0]
print(evens)

lst=[7,8,9,4,3,2]
op=[ num+1 if num>5 else num-1 for num in lst]
print(op)

employees=[
    {"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    {"eid": 1001, "name": "vijay", "salary": 22000, "designation": "developer"},
    {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
     {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},

]
#employees names
enames=[emp["name"] for emp in employees]
print(enames)

#developes name
developer=[emp for emp in employees if emp["designation"]=="developer"]
print(developer)

#highest salary
max_salary=max([emp["salary"] for emp in employees])
print(max_salary)
