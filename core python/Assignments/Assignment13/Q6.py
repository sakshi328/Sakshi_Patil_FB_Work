#python program to multiply all the items in a dictionary
d={"a":10, "b":20, "c":30}
mul=1

for x in d.values():
    mul=mul*x
print("sum=", mul)