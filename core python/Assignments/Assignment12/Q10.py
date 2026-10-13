#python program to take in two strings and display the larger string without using built-in function
str1=input("Enter first string: ")
str2=input("Enter second string: ")

count1=0
count2=0

for ch in str1:
    count1+=1
    
for ch in str2:
    count2+=1

if count1>count2:
    print("Larger string:", str1)

elif count2>count1:
    print("Larger string:", str2)
else:
    print("Both strings are equal")
    