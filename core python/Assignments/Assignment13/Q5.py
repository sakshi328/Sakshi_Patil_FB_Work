#python program to sum all the items in a dictionary
d={"a":10, "b":20, "c":30}
total=0

for x in d.values():
    total=total+x
print("sum=", total)