#Write a program to count the number of words in a
#string.

string=input("Enter the string: ")
substring=input("Enter the word: ")

lis=string.split()
print(lis)
count=0
for x in lis:
    if x == substring:
        count+=1
print(count)