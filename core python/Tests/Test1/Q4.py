wall_area=float(input("Enter the area of one wall:"))
cost_interior=float(input("Enter the cost interior:"))
cost_exterior=float(input("Enter the cost exterior:"))

interior=wall_area*cost_interior
exterior=wall_area*cost_exterior

total=interior+exterior

print("Interior painting cost=", interior)
print("exterior painting cost=", exterior)
print("Total painting cost=", total)