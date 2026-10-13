#python program to detect if two string are Anagrams
str1=input("Enter the word: ")
str2=input("Enter the word: ")
if sorted(str1)==sorted(str2):
    print("It is Anagram")
else:
    print("It is not Anagram")