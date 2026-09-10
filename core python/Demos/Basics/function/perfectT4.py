def perfect(num):
    sum=0
    for i in range(1,num):
        if(num%i==0):
            sum=sum+i
    if(sum==num):
        return("Perfect number")
    else:
        return("not perfect number")
num=int(input("Enter number:"))
res=perfect(num)
print(res)