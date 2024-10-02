#8. Check if a given string is a palindrome (reads the same
#backward as forward).

string=input('Enter your string: ')
temp=string
string=string[::-1]
if string==temp:
    print('The given string is a pallindrome')
else:
    print("This is not a pallindrome")