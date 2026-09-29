def Anagram_check(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()
    if sorted(str1)==sorted(str2):
        return True
    else:
        return False
str1=input("Enter first string:")
str2=input("Enter second string:")
print("The strings are anagrams") if Anagram_check(str1,str2) else print("The strings are not anagrams")