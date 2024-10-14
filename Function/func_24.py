#24.Write a recursive function reverse_string_recursive(s) to reverse a string.

def reverse_string_recursive(s):
    if len(s)==0:
        return s
    else:
        return s[-1]+reverse_string_recursive(s[:-1])
    

print(reverse_string_recursive("hello"))