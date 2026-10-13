#python program to count the number of vowels in a string
str=input("ENter the word: ")
count=0
for ch in str:
    if ch in "aeiou":
       count= count+1
print("Number of vowels:", count)