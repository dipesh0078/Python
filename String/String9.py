#Write a program that checks if a substring exists within a
#string.

string=input("Enter your string: ")
list=string.split()
check=input('substring to check: ')
if check in list:
    print('It is present')
else:
    print('It is not present in the string')