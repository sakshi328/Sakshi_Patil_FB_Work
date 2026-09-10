def armstrong(num):
    temp=num
    sum=0
    digits=len(str(num))
    while(num>0):
        digit=digits%10
        sum=sum+digit*digits
        num=num//10
    if sum==temp:
        print("Armstrong number")
    else:
        print("Not Armstrong number")
        
num=int(input("Enter number:"))
armstrong(num)