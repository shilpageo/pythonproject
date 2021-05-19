#EXCEPTION HANDLING
#-------------------

#{try and finally always work
#.............................}


#normal
#num1=int(input("enter no"))
#num2=int(input("enter a no"))
#print(num1/num2)

#excption case[zero division error]

a=int(input("enter a no"))
b=int(input("enter a no"))

try:
    print(a)
    print(a/b)

except:
    print("exception occured")

finally:
  print("inside finally")
