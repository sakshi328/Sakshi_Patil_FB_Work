#WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.[T-1]
def armstrong():
    num=int(input("Enter number:"))
    temp=num
    sum=0
    digits=len(str(num))
    while(num>0):
        digit=num%10
        sum=sum+digit**digits
        num=num//10
    if sum==temp:
        print("Armstrong number")
    else:
        print("Not Armstrong number")
armstrong()