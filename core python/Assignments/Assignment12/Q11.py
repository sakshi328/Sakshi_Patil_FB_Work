#python program to count number of lowercase characters in a string
str=input("Entter the string:")
count=0
for ch in str:
   if ch.islower():
      count= count+1
print(count)