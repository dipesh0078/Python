#Write a Python program that replaces all occurrences of
#a substring within a string with another substring.

string=input('Enter your string: ')
rep=input('Enter your replacement substring: ')
target=input('Enter your target substring: ')
replaced=string.replace(target, rep)
print()
print(replaced)