#9. write a program of having a number of elements in the list and find out even and odd elements in that list 
# and then create two seperate lists which will have even elements and other will have odd elements.
li=[2,4,8,6,1,3,7]
even=[]
odd=[]
for i in range(0,len(li)):
    if li[i]% 2==0:
        even.append(li[i])
    
    else:
        odd.append(li[i])
print("Even number:",  even)
print("Odd number:", odd)