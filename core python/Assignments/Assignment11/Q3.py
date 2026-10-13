#python program to sort the list according to the second element in sublist
li=[[1,50], [2,20],[3,40],[4,10]]

li.sort(key=lambda x:x[1])
print(li)