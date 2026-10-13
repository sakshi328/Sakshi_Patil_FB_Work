#Write a python program to find all the unique words and count the frequency of occurences from a given list of string. use python set data types
list=["apple", "mango", "apple", "banana", "mango", "apple"]
s=set(list)

for i in list:
    count=list.count(i)
    print(i,":", count)
