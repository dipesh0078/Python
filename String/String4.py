#Convert a given string to all uppercase and then replace all
#occurrences of the letter 'A' with the character '@'.

string=input("Enter your string: ")

string=string.upper()
string=string.replace('A','@')
print(string)