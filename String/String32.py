#Write a program to find the shortest word in a string.
string = input("Enter your string: ")

ls=string.split()
min=ls[0]
for x in ls:
    if len(x)<len(min):
        min=x

print(min)