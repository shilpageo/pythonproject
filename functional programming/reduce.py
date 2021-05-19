#reduce must be import
#map filter 1 arg
#lambda 2 arg
#reduce 2 arg
import functools
lst=[7,8,9,4,3,2]
total=functools.reduce(lambda no1,no2:no1+no2,lst)
print(total)

max=functools.reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)
print(max)

