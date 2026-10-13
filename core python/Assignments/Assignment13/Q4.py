#python program to generate a dictionary that contains numbers(between 1 and n) in the form (x,x*x)
n=int(input("Enter a number:"))
d={}

for x in range(1,n+1):
    d[x]=x*x
print(d)