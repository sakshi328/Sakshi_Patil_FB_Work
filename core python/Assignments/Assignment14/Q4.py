#write a python program that finds all pairs of elements in a list whose sum is equal to a given value 
li=[2,4,3,5,6,7,8]
n=9

for i in range(len(li)):
    for j in range(i+1, len(li)):
        if li[i]+li[j]==n:
            print(li[i],li[j])