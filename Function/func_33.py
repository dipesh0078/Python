#33.Write a lambda function to check if a given string is a palindrome.

pallindrome=lambda s: True if s==''.join(reversed(s)) else False

print(pallindrome('lalal'))