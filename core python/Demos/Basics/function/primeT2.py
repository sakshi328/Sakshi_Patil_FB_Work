def prime(num):
    for i in range(2,num):
        if num%i==0:
            print("Not Prime")
            break
    else:
        print("Prime number")
num=int(input("Enter number:"))
prime(num)
    