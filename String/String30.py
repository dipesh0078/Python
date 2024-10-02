#Write a Python program that checks if a string starts
#and ends with the same character.


string=input("Enter your string: ")
l=len(string)
if string[0]==string[l-1]:
    print("This string starts and ends with the same character")
else:
    print("This string starts and ends with the different character")