pattern="ABCDBAC"
dict={}
for char in pattern:
    if(char not in dict):
        dict[char]=1
    else:
        print(char)
        break
