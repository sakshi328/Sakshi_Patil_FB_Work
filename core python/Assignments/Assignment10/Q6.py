#6. WAP to remove duplicate from the list.
li=[10,50,50,20,20,70]
new_li=[]
for i in range(0,len(li)):
    if li[i] not in new_li:
        new_li.append(li[i])
print("List after removing duplicates:", new_li)
