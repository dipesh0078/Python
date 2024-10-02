#Find the longest word in a given string.

string=input('Enter your string: ')
l=[]
l=string.split()
max=''
for x in l:
    if len(x)>len(max):
        max=x
print(max)