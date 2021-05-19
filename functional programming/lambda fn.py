#lambda keyword is used

#ad=lambda num1,num2:num1+num2
#print(ad(10,20))



#function
#---------

#def sub(num1,num2):
 #   return num1-num2

#lambda function
#----------------

#sub=lambda num1,num2:num1-num2
#print(sub(20,13))

#mul=lambda num1,num2:num1*num2
#print(mul(10,20))

#div=lambda num1,num2:num1/num2
#print(div(10,20))


lst1=[7,8,9,4,3,1]
#if num>5 num+1
#else num=1
#[8,9,10,3,2,0]-output

#lst=[10,20,21,22,23]
#lst2=[20,21,10,22,23]
#check for given two list are same or not

#map()         {used in list}
#used to filter data without any specific condition
#filter        {used in list}
#used to filter data using specific conition
#reduce

#map example

lst=[2,3,4,5,6,7]
squares=list(map(lambda num:num**2,lst))
print(squares)

names=["ajay","aravind","arun"]

upp=list(map(lambda name:name.upper(),names))

print(upp)



