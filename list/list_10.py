#10. How do you reverse a list using indexing? 

my_list=[1,2,3,4,5,6,7,8]

#To reverse a list using indexing in Python, we can use slicing with a step of -1. 
# This creates a new list that starts from the end and goes to the beginning.

reversed_list=my_list[::-1]
print(reversed_list)

#uisng reverse() method:

my_list.reverse()
print(my_list)