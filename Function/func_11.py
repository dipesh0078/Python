#11.Write a function capitalize_words(s) that capitalizes the first letter of
#each word in the string s.

def capitalize_words(s):
    return ' '.join([word.capitalize() for word in s.split()])

string=input("Enter your string: ")

print(capitalize_words(string))


