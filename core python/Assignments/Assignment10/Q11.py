#11. write a program to print all numbers which are divisible by m and n in the list
li=[10,11,24,30,40,15,18]
m=2
n=3
for i in range(len(li)):
    if li[i]%m==0 and li[i]%n==0:
        print(li[i])