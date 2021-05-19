str='hell$#%o w*&or@!ld'
a=''
char="!@#$%^&*():_+{}|<>?/.,';\][=-"
for i in str:
    if(i not in char):
        a+=i
print(a,end=" ")

