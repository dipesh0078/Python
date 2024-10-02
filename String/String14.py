#Check if two strings are anagrams of each other
#(contain the same letters in different orders).
string1=input("Enter 1st string: ").replace(' ','').lower()
string2=input("Enter 2nd string: ").replace(' ','').lower()

if sorted(string1)==sorted(string2):
    print("The strings are anagrams")
else:
    print('The strings are not anagrams')