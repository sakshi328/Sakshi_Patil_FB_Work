n=int(input("Enter the number:"))
temp=n
sum=0
digits=len(str(n))
while(n>0):
    digit=n%10
    sum=sum+digit**digits
    n=n//10
if sum == temp:
    print("Armstrong number")
else:
    print("Not armstrong number")