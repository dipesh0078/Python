#12. How do you find the index of a particular element in a list? 

#To find the index of a particular element in a list, we can use the index() method. This method returns the first index at which the specified element is found. 
# If the element is not present, it raises a ValueError.

my_list=[1,2,3,4,5]

index=my_list.index(5)
print(index)

