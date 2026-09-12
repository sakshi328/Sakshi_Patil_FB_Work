# 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.
n=int(input("Enter number of students:"))
total_percentage=0
for i in range(n):
    total=0
    for j in range(5):
        marks=int(input("Enter marks"))
        total=total+marks
    percentage=total/5
    print("percentage=", percentage)
    
    total_percentage=total_percentage+percentage
    
    average=total_percentage/n
    print("Average percentage=", average)