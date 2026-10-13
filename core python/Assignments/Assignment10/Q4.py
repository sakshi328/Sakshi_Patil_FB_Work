#4. write a program to reverse the list
li=[20,50,30,40,10,90]
rev=[]
for i in range(len(li)-1,-1,-1):
    rev.append(li[i])
print("Reversed list:",rev)