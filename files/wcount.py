f=open("sample3","r")


dict={}
for i in f:
    word=i.rstrip("\n").split(" ")
    for a in word:
      if a not in dict:
        dict[a]=1
      elif a in dict:
       dict[a]+=1
print(dict)