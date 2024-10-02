#Write a Python program that counts the number of vowels in
#a given string.

vowels=['a','e','i','o','u']
count=0
string=input("Enter your string: ")
string1=string.lower()
for x in string1:
    if x in vowels:
        count+=1
print(f'{count} number of vowels are in the string: {string}' )
