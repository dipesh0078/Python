#Write a program that removes punctuation from a
#string.

punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
original_string = input("Enter your string: ")
result_string = ""

for char in original_string:
    if char not in punctuation:
        result_string += char
print("String after removing punctuation:", result_string)