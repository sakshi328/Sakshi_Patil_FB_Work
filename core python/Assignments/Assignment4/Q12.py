#12. Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# 4*4*4*4)

num=int(input("Enter the number"))
temp=num

sum=0
digit=len(chr(num))

while(num>0):
    digit=num%10
    sum=sum+digit**digit
    num=num//10
    
if sum==temp:
    print("Armstrong number")
    
else:
    print("Not an Armstrong Number")