# for i in range(1,6):
#     for j in range(1,6):
#         if i%2==0:
#             print("$", end=" ")
        
#         else:
#             print("*", end=" ")
#     print()          


for i in range(6,1):
    for j in range(1-i):
        print(" ", end=" ")
    for j in range(1, 7-i):
        print("*", end=" ")
    
    print()
    
    