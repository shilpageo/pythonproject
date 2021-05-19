#split line of data can be split into word by word

line="hai hello hai hello"
words=line.split(" ")


dict={}
count=0
for i in words:
  if i not in dict:
    dict[i]=1
  elif i in dict:
     dict[i]+=1
print(dict)