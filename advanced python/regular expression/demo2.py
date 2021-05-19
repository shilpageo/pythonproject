import re
n='hello'
x='\w*'         #* means zero or more
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")


#finditer--consider each wrd
#fullmatch--consider fully


import re

n = '57kg'
x = '\d{2}[a-z]{2}'
match = re.fullmatch(x, n)
if match is not None:
    print("valid")
else:
    print("invalid")

import re

n = input("enter no")
x = '\d{10}'  # * means zero or more
match = re.fullmatch(x, n)
if match is not None:
    print("valid")
else:
    print("invalid")

import re

n = input("enter no")
x = '[+]\w[9][1]\d{10}'  # * means zero or more
match = re.fullmatch(x, n)
if match is not None:
    print("valid")
else:
    print("invalid")


