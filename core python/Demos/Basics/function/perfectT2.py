def perfect(num):
    sum=0
    for i in range(1,num):
        if(num%i==0):
            sum=sum+i
    if(sum==num):
        print("Perfect number")
    else:
        print("Not perfect number")
num=int(input("Enter number:"))
perfect(num)