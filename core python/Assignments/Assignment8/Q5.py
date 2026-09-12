# 5. Sum of all prime numbers between 1 to n(T-3)
def prime():
    num=int(input("Enter number:"))
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count +=1
    
    if count ==2:
        return "Prime number"
    else:
        return "Not Prime Number"

result=prime()
print(result)