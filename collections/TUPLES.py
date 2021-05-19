#TUPLES
#--------

tp=()
#print(type(tp))

tp=tuple()  #using function

#PROPERTIES
#-----------
tp1=(1,10.5,"shilpa",True,False)   #support hetrogenous data
print(tp1)

tp2=(1,2,3,4,"luminar","abcd",True)  #insertion order preserved
print(tp2)

tp3=(1,1,2,2,True,"luminar")   #support duplication
print(tp3)

tp3(2)=10    #cannot read index value[tuple is immutable][cannot add or remove elements]
print(tp3)