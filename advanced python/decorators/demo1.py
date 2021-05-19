#to add feature in an existing function
def shuffle_values(func): #here defines the func sub,div [1]
    def wrapper(no1,no2):     #[3]
        if no1<no2:            #[4]
            (no1,no2)=(no2,no1)  #[5]
        return func(no1,no2)      #[6]
    return wrapper  #[2]


@shuffle_values       #[7]
def div(num1,num2):
    return num1/num2


@shuffle_values
def sub(num1,num2):
    return num1-num2

print(div(2,10))
print(sub(10,30))