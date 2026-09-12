#6. Write a program to print first n prime numbers.
n=int(input("enter number:"))
num=2
count=0
while count <0:
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num, end=" ")
    num +=1