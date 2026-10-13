#python program to remove the character of odd index values in a string.
str=input("Enter the string:")
new_str=" "

for i in range(0,len(str)):
    if i%2==0:
        new_str=new_str+str[i]
print(new_str)