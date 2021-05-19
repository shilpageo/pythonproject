#re package used[re means regular expression]

import re
count=0
matcher=re.finditer('ab','abbabbab')
print(matcher)
for match in matcher:
    count+=1
print("count",count)


#start to find index where is match available[return position]
#group which object find match

import re
count=0