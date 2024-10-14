#8. Write a function count_vowels(s) that returns the number of vowels
#in the string s.

def count_vowels(s):
    vowels=['a','e','i','o','u']
    count=0
    for i in s:
        if i in vowels:
            count+=1
    return count


string=input("Enter your string: ")

print(count_vowels(string))