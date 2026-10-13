#10. write a program to remove all occurrences of a given element in the list
li=[10,20,60,20,40,20]
element=20
newli=[]
for i in range(len(li)):
    if li[i]!=element:
        newli.append(li[i])
print(newli)