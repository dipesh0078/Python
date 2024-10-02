#Write a program to remove duplicate characters from a
#string while preserving the order of characters.

original_string = input("Enter your string: ")
result_string = []
original_string=original_string.split()
for char in original_string:
   if char not in result_string:
        result_string.append(char)
result_string=' '.join(result_string)
print("String after removing duplicates:", result_string)