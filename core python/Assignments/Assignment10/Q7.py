#7. write a program to create a new list from existing list which contain cube of each number of list
li=[2,5,4,6,8,3]
new_li=[]
for i in range(0,len(li)):
    cube=li[i]**3
    new_li.append(cube)
print("cube:", new_li)