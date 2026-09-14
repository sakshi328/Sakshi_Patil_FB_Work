num=int(input("Enter number:"))
if 100<=num <=999:
    d1=num//100
    d2=(num//10)%10
    d3=num%10
    
    if d1==(2*d2) and d1==(d3/2):
        print("Yes, you have done it")
    else:
        print("Please try next time")
else:
    print("Invalid input! please enter valid number")