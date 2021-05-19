employees=[
    {"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
     {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},

]
developers=list(filter(lambda emp:emp["designation"]=="developer",employees))
print(developers)

developers_name=list(map(lambda emp:emp["name"],employees))
print(developers_name)
emp_names=list(map(lambda emp:emp["name"],employees))
print(emp_names)
#___________________________________________
#even no
#lst=[2,3,4,5,6,7]
#evens=list(filter(lambda number:number%2==0,lst))
#print(evens)

#filter number >5
#nums=list(filter(lambda number:number>5,lst))
#print(nums)