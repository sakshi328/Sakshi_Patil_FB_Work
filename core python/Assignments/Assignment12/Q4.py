#python program to form a new string where the first chracter and the last character have been exchanged
s=input("Enter a string:")
new_s=s[-1]+s[1:-1]+s[0]
print(new_s)