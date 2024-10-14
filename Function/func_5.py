#5. Write a function reverse_string(s) that returns the reverse of the input
#string s.

def reverse_string(s):
    new=s[::-1]
    return new


string=input('Enter your string: ')

print(reverse_string(string))