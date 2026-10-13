#Python Program to count the frequency of words appearing in a string using a dictionary
di=input("Enter a string:")
words = di.replace(",", " ").split()

di={}

for i in words:
    if i in di:
        di[i]+=1
    else:
        di[i]=1
        
print(di)