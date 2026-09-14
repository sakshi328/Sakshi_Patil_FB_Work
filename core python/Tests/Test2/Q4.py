length = float(input("Enter length of wall: "))
height = float(input("Enter height of wall: "))
cost = float(input("Enter painting cost per square unit: "))

area = 4 * length * height
total_cost = area * cost

print("Total cost of painting =", total_cost)