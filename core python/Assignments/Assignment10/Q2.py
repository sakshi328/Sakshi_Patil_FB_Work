#2.Write a program to find maximum element in a list
li=[50,40,60,30,70,80]
max_num=0
for i in range(1,len(li)):
    if li[i]>max_num:
        max_num=li[i]
print("Maximum number:", max_num)
    