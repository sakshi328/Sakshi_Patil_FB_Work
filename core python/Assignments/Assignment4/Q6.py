#6. WAP to check if a given number is prime number or not.
num=int(input("Enter the number:"))
count=0
for i in range(1, num+1):
    if num%i==0:
        count=count+1

if count==2:
    print("Prime number")

else:
    print("Not a prime number")