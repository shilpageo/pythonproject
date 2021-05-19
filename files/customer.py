f=open("/home/shilpa/Downloads/customer")
for lines in f:
    data=lines.rstrip("\n").split(",")
    #print(data)
#name age country retrive using index values
    fname=data[1]
    lname=data[2]
    age=data[3]
    cou=data[-1]
    prof=data[4]
    #print(fname,",",age,",",cou)
    #if cou=="india":
     #   print(fname,",",age,",",cou)
    #if age>"50":
    #    print(fname, ",",lname,"," ,age, ",",prof, ",",cou)
    if (prof=="doctor"):
        print(fname, ",", lname, ",", age, ",", prof, ",", cou)