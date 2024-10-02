#Write a Python program that counts how many times
#each vowel appears in a given string.
original_string = input("Enter your string: ")
vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}


original_string = original_string.lower()
for char in original_string:
    
    if char in vowel_count:
        vowel_count[char] += 1  
print("Vowel counts:")
for vowel, count in vowel_count.items():
    print(f"{vowel}: {count}")