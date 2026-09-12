#4. WAP to print Armstrong number within a given range
n=int(input("Enter number:"))
temp=n
sum=0
digits=len(chr(n))
while(n>0):
    digit=n%10
    sum=sum+digits*digits
    n=n//10
    
if sum==n:
    print("Armstrong")
    
else:
    print("not armstrong ")