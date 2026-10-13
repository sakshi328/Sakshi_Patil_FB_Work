#python program to find the second largest number in list using bubble sort
li=[50,40,30,20,10]

for i in range(0,len(li)-1):
    for j in range(0, len(li)-1-i):
        if li[i]>li[j+1]:
            li[i],li[j+1]=li[j+1],li[i]
print("Second largest:", li[-2])