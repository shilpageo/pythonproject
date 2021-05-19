#nested list

lst=[[1001,"arjun",25,1000],
    [1002,"arun",26,2000],
    [1003,"vinu",27,3000],
    [1004,"binu",28,4000]]

#for emp in lst:
    #print(emp)   #iterate all
    #print(emp[1])   #print emp names
    #if (emp[3]>2000):
      # print(emp[1])   #salary above 2000

sum=0
for emp in lst:
    sum=sum+emp[3]