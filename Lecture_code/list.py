#List : group o felements where insertion order is preserved and duplicate are allowed


#By using while loop traversing

l=[10,20,30,40,50,60]
i=0
while i<len(l):
    print(l[i], end=' ')
    i=i+1

print()
#By using for loop
l2=['a','b','c','d']
for x in l2:
    print(x,end=' ')


print()
#counting elements in list ,length of list and index
l3=[1,2,3,4,2,1,1,2,31,1]
print(l3.count(1))
print()
print(len(l3))
print()
print(l3.index(31))
print()


#manipulating list

l4=[1,2,3,1,23,4,5,6]
#append
l4.append(90)
print(l4)

l5=[]
for i in range(101):
    if(i%10==0):
        l5.append(i)
print(l5)

#insert function in list
print()
l5.insert(1,1000)
print(l5)

#extend function
l6=[10,20,30,40,60,60]
l7=['A','B','c']
l6.extend(l7)
print(l6)
n="Hari"
l7.append(n)
print(l7)
print()

#remove()
print()
l7.remove('A')
print(l7)

l8=[1,2,3,4,1,2,1,2,3,4,5]
#x=int(input("Enter number to remove: "))
#while True:
#    if x in l8:
#        l8.remove(x)
#    else:
#        break
#print(l8)
#print()

#pop()
l7.pop()
print()
print(l7)

#string reverse
print(l4)
l4.reverse()
print()
print(l4)
a=reversed(l4)
print(a)

print()


my_strings = ["apple", "banana", "cherry", "date"]
my_strings.sort(key=len)  # Sort by length of the strings
print(my_strings)


#Aliasing and cloning of list

x=[10,20,30,40]
y=x
print()
print(id(x))
print(id(y))
y[2]=500
print(x)
print(y)

#so we need cloning
y=x[:]
print(id(x))
print(id(y))
y[2]=600
print(x)
print(y)

#to remove a list list.clear

#Mathmetical operator

x=[10,20,30,40]
y=[100,200]
print(x+y)

#list compherension : process of creating list from other sequence (condition not mandetory)

c=[i for i in range(1,11)]
print(c)