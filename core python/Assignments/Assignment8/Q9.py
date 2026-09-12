#Write a program to check if entered number is a palindrome or not.
def palindrome(num):
    temp=num
    rev_num=0
    while(temp>0):
        d=temp%10
        temp=temp//10
        rev_num=rev_num*10+d
    if(rev_num==num):
        print("Pallindrome number")
    else:
        print("Not pallindrome")
num=int(input("enter number:"))
palindrome(num)