#12. Write a program to create three lists of numbers, their squares and cubes
li=[2,3,4,5,6]
squares=[]
cubes=[]
for i in range(len(li)):
    square=li[i]**2
    squares.append(square)
    cube=li[i]**3
    cubes.append(cube)
print(li)
print(squares)
print(cubes)