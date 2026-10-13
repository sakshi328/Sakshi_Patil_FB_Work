#5.Accept a number from user and check if this element is present in the list or not. ALso tell how many times it is present in the list
li=[40,60,80,90,50,50,10]
num=int(input("Enter number:"))
count=0
for i in range(0,len(li)):
    if li[i]==num:
        count=count+1
if count>0:
    print("Element is present")
    print("IT is present", count, "times")
else:
    print("Element is not present")
    