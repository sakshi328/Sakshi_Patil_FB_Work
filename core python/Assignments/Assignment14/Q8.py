#write a python program to find all the anagrams and group them together from a given list of strings.

li=["eat", "tea", "tan","ate", "nat", "bat"]
di={}
for word in li:
    key=''.join(sorted(word))
    
    if key not in di:
        di[key]=[]
        
    di[key].append(word)
    
print(list(di.values()))