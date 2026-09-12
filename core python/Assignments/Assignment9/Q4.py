#4. Write a program to find sum of n numbers using recursion.
def sum_OF_series(n):
    if(n<=0):
        return 0
    else:
        return(n+sum_OF_series(n-1))
    
n=int(input("Enter number:"))
res=sum_OF_series(n)
print(res)