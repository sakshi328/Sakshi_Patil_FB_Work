def prime():
    num=int(input("Enter number:"))
    for i in range(2,num):
        if(num%i==0):
            return(f'{num} is not a prime number' )
            
    else:
        return(f'{num} is a prime number')
    
print(prime())
        
