#Write a Python program that finds all occurrences of
#the letter 'a' in the string "banana" and prints their positions.

string='banana'

pos=[]
for index, letter in enumerate(string):
    if letter=='a':
        pos.append(index)
print(pos)