#13.Write a to print list after removing even numbers.
li=[42,3,4,5,6,8]
newli=[]
for i in range(len(li)):
    if li[i]%2==0:
       newli.append(li[i])
print(newli)