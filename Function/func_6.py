#6. Write a function is_palindrome(s) that checks if the input string s is a
#palindrome.

def is_palindrome(s):
    temp=s[::-1]

    if s==temp:
        return True
    else:
        return False
    

string=input('Enter your string: ')

print(is_palindrome(string))