#swap two number without using third variable

x=10
y=20

print(f'before swapping x:{x}, y:{y}.')

#x, y=y, x
#y, x=x, y

x=x+y
y=x-y
x=x-y

print(f'after swapping x:{x}, y:{y}.')