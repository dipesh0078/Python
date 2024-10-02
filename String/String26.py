#Write a program that concatenates two strings without
#using the + operator.

string1=input("Enter your string1: ")
string2=input("Enter your string2: ")
ls1=string1.split()
ls2=string2.split()
for x in ls2:
    ls1.append(x)
print(ls1)
final=' '.join(ls1)
print(final)