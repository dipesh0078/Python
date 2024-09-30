s='abcdefghijkl'
print(s[1:6:1])
print(s[::1])
print(s[::-1])
print(s[3:7:-1]) #blank 
print(s[7:4:-1])
print(s[-4:1:-1])
print(s[3:700])

a='apple'
b='apple'
print(a==b)
print(a<b)
print(ord('a'))


#lstrip() rstrip() strip()
#name=input("Enter your name ").strip() #chaining of function
#if name.lower()=='hari':
 #   print("You are welcome")
#else:
#    print("SORRY")

#find rfind index rindex

value='Learning python is fun'

print(value.find('r'))
print(value.rfind('p'))
print(value[7:60].find('i'))
print(value.find('i',7,60))
#print(value.index('fy')) #error dincha index le chai
print(value.count('i',10,15))


#replacing substring

c='Python is beautiful'
print(c.replace('beautiful','easy'))

#splitting of string
s="Hi my name is dipesh thapa"
print(s.split())

date='2058-1-2'.split('-')
print(date)

#joint

l=['Hello','this', 'is', 'very','intresting']
a=' '.join(l)
print(a)


#changing case of string ( upper(), lower(), swap)
test='leARniNg is fun'
print(test.upper())
print(test.lower())
print(test.swapcase())
print(test.title())
print(test.capitalize())


#checking starting and ending part of string  [ startswith(), endswith()]

t="learning is fun"
print(t.startswith('l'))
print(t.startswith('learning'))
print(t.endswith('l'))
print(t.endswith('fun'))
print(t.endswith('n'))

#To check type of characters present in a string isalpha(), isalnum, isdigit(), isupper(), islower(), isspace()
print()
print('Learning python 3.12 '.isalnum())
print('Learning python312 '.isalnum())
print('Learning python 3.12 '.isalpha())
print('312'.isdigit())


#string formatting

d='dipesh'
caste='Thapa'

print(f'My name is {d} {caste}')
print('My name is {0} and my caste is {1}'.format(d,caste))
print('My name is {a} and my caste is {b}'.format(a=d,b=caste))
print('The integer numer is {}'.format(123))
print('The integer numer is {:5d}'.format(123))
print('The integer numer is {:05d}'.format(123))