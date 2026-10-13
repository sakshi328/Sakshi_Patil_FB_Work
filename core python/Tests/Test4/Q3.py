#3
rows = 10
cols = 21

for i in range(1, rows + 1):
  for j in range(1, cols + 1):
    # Top row, bottom row, ya phir diagonal formula
    if i == 1 or i == rows or j == cols - int((i - 1) * (cols - 1) / (rows - 1)):
      print("*", end="")
    else:
      print(" ", end="")
  print()