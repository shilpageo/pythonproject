#add

#def add(num1,num2):  #parameter(par1,par2)
#    return num1+num2


#res=add(10,20) #actual value is argument(arg1,arg2)
#print(res)





# addThree() camalin notation --used in jscript|
#add_three()                  --used in python |

def add(*args):  #10,20  #here type of *args is tuple and if **args is dictionary
    res=0
    for num in args: #10
        res+=num #res=0+10=10=10+20=30
    return res  #30

print(add(10,20))    # {arg always in tuple form}

#arr.sort() ----sort is a method
#def new_sorted()---function


arr=[2,8,6,7,10,6]
data=sorted(arr,reverse=True)
print(data)


def print_employee(**kwars):
    print(kwars)
print_employee(id=1000,name="ajay",salary=5000)

#create a function print_employee()=>scalling fn print_employee(id=1000) it will name of that employee

#print_employee(id=1000)=>ajay
#print_employee(id=1000,prop="salary")=>ajay,25000
#print_employee(id=1001,prop="designation")vijay,developer

employees=employees={
    1000:{"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    1001: {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    1002: {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    1003: {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
    1004: {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},

}


def print_employee(**kwargs):   #kwargs={id:1000}   [ _ is given as to the coding standard]
    id=kwargs["id"]   #1000
    prop=kwargs["prop"] #salary
    if id in employees:  #1000 in employee
      print(employees[id]["name"]) #employees[1000]
      print(employees[id][prop])
    else:
        print("invald id")
print_employee(id=1003,prop="salary")


# coding standards in python
# NUMBER number

