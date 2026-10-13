# python program to put even and odd elements of a list into two different lists
li=[10,15,20,25,30,35]
even=[]
odd=[]

for i in li:
    if i % 2==0:
        even.append((i))
    
    else:
        odd.append(i)
print("Even elements:", even)
print("Odd elements:", odd)