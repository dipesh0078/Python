#Write a program to find the frequency of each character
#in a string.
original_string = input("Enter your string: ")
frequency = {}
for char in original_string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character frequency:")
for char, count in frequency.items():
    print(f"'{char}': {count}")