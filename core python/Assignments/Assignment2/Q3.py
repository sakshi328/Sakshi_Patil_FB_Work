#convert distant given in feet and inches into meter and centimeter
# 1foot=0.3048
# 1inch=2.54 centimetre
feet=float(input("Enter feet:"))
inches=float(input("Enter inches:"))

meter= feet*0.3048
centimeter=inches*2.54

print("Distance in meter=", meter)
print("Distance in centimeter=", centimeter)