#Write a Python program to convert a string from
#snake_case to camelCase.


snake_case_string = input("Enter a string in snake_case: ")
words = snake_case_string.split('_')
camel_case_string = words[0] + ''.join(word.capitalize() for word in words[1:])
print("String in camelCase:", camel_case_string)