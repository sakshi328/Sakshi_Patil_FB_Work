#write a program to accept distance in Km and convert it into meters and centimeter
kilometers=float(input("Enter distance in kilometer:"))
meters=kilometers*1000
centimeters=kilometers*10000

print(f"{kilometers} kilometer is equivalent to")
print(f"{meters:} meters")
print(f"{centimeters} centimeter")