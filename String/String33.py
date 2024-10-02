#Write a Python program that finds and prints the
#longest repeated substring in a given string.
# Get input from the user
original_string = input("Enter your string: ")

n = len(original_string)
longest_substr = ""
for i in range(n):
    for j in range(i + 1, n):
        length = 0
        while (j + length < n and original_string[i + length] == original_string[j + length]):
            length += 1
        if length > len(longest_substr):
            longest_substr = original_string[i:i + length]


if longest_substr:
    print("Longest repeated substring:", longest_substr)
else:
    print("No repeated substring found.")
