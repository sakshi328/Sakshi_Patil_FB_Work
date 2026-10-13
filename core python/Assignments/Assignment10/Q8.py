#8.Write a program to create a duplicate of an existing list. it should not point to same list.
li=[10,20,30,40,50,6]
duplicate=li.copy()
print("Original list:", li)
print("Duplicate list:", duplicate)