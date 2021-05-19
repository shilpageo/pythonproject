#import re
#x="[abc]"   #either a,b or c
#matcher=re.finditer(x,"abt c@5kz")
#for match in matcher:
 #   print(match.start())
 #   print(match.group())

#import re
#x = "[^abc]"  # except a,b or c
#matcher = re.finditer(x, "abt c@5kz")
#for match in matcher:
 #   print(match.start())
  #  print(match.group())

import re
x="[a-z]"   #conisder only small letter
matcher=re.finditer(x,"AvgBT12")
for match in matcher:
    print(match.start())
    print(match.group())

import re
x="[A-Z]"   #conisder only capital letter
matcher=re.finditer(x,"AvgBT12")
for match in matcher:
    print(match.start())
    print(match.group())

import re
x="[a-zA-Z]"   #conisder both caps and small letter
matcher=re.finditer(x,"AvgBT12")
for match in matcher:
    print(match.start())
    print(match.group())

import re
x="[0-9]"   #conisder only numbers
matcher=re.finditer(x,"AvgBT12")
for match in matcher:
    print(match.start())
    print(match.group())

import re
x="[a-zA-Z0-9]"   #conisder small letter uppcase and numbers
matcher=re.finditer(x,"AvgBT12")
for match in matcher:
    print(match.start())
    print(match.group())

import re
x="[^a-zA-Z0-9]"   #consider only special symbols
matcher=re.finditer(x,"9*8AsDc@")
for match in matcher:
    print(match.start())
    print(match.group())

import re
x="\s"   #check spaces
matcher=re.finditer(x,"Avg BT1 2")
for match in matcher:
    print(match.start())
    print(match.group())

import re
x="\d"   #checks digits
matcher=re.finditer(x,"AvgBT12")
for match in matcher:
    print(match.start())
    print(match.group())
    #rules programs
import re
x="\D"   #except digits
matcher=re.finditer(x,"AvgBT12")
for match in matcher:
    print(match.start())
    print(match.group())

import re
x="\w"   #all words except special characters
matcher=re.finditer(x,"A!vg@BT12")
for match in matcher:
    print(match.start())
    print(match.group())

import re
x="\w"   #for special characters
matcher=re.finditer(x,"AvgBT12")
for match in matcher:
    print(match.start())
    print(match.group())