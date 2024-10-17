#3. How do you remove an element from a set?

#remove()
#Removes the specified element from the set.
#Raises a KeyError if the element is not present.
my_set={1,2,3,4}
my_set.remove(4)
print(my_set)

#discard()
#Removes the specified element from the set.
#Does not raise an error if the element is not present.
my_set.discard(7)


#pop()
#Removes and returns a random element from the set.
#Raises a KeyError if the set is empty.

element=my_set.pop()
print(element)

#clear()
#removes all elements from the set
my_set.clear()
print(my_set)