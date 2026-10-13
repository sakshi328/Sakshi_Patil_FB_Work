#python program to count number of digit and letter in a string
str=input("Enter a string:")

digit=0
letter=0
for i in str:
    if i.isdigit():
        digit+=1
    elif i.isalpha():
        letter +=1
print("Number of digits:", digit)
print("Number of letters:", letter)