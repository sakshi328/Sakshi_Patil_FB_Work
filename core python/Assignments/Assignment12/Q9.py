#python program to calculate the number of words and the number of character present in a string
str=input("Enter a string: ")

char_count=0
word_count=1
for i in str:
    char_count=char_count+1
    
    if i==" ":
        word_count=word_count+1
print("Number of characters:", char_count)
print("Number of words:", word_count)   