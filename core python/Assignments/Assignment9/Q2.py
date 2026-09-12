# 2. Write a program to check if given number is Armstrong or not using recursive
# function.
def armstrong(tem,num,count,sum=0):
    if tem==0:
        if num==sum:
            print("Armstrong number")
        else:
            print("Not Armstrong number")
        return
    d=tem%10
    sum=sum+d**count
    armstrong(tem//10,num,count,sum)
num=int(input("Enter number:"))
tem=num
count=len(str(num))
armstrong(tem,num,count)