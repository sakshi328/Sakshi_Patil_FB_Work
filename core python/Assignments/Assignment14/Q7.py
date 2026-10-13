#Given two seats of numbers, write a python program to 
# find the missing numbers in the second set as
# commpared to the first and vise versa. 
# use the python set.
# Find missing numbers in both sets using set

s1 = {1, 2, 3, 4, 5}
s2 = {2, 4, 6, 8}

print("Missing in second set:", s1 - s2)
print("Missing in first set:", s2 - s1)