#Write an algorithm to find a maximum number in a given list
li=[40,50,30,60,20,10]
max_num=li[0]
for i in range(1,len(li)):
    if li[i]>max_num:
       max_num=li[i]
     
print("Maximum number:",  max_num)
     
    
    
    