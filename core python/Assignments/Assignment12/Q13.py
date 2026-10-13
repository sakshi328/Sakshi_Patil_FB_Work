#python program to count the occurrences of each word in a string
str=input("Enter a string:")
words=str.split()
count={}
for word in words:
    if word in count:
        count[word]+=1
    else:
        count[word]=1
print(count)