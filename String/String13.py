#Write a program to compare two strings
#lexicographically and determine which one comes first
#alphabetically.

string1=input('Enter 1st string: ')
string2=input("Enter 2nd string: ")

if string1 > string2:
    print('String2 comes before String1')
elif string1 < string2:
    print('String1 comes before String2')
else:
    print('Both strings are the same')