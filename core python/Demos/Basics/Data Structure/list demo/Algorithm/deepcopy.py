import copy
li=[[10,20],[30,40]]
b=copy.deepcopy(li)
b[0][0]=100
print(li)
print(b)