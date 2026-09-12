for i in range(1,6):
    for j in range(1,11):
        if(i+j==6 or j-i==4):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(1,6):
    for j in range(1,10):
        if i==j or i+j==10:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()