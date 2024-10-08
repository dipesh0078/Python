#15. How can you access a list in reverse order without modifying it? 

#using slicing method :

my_list=[1,2,3,4,5,6]

reversed_list=my_list[::-1]

print(reversed_list)

#using reversed() function:

reversed_list_2=list(reversed(my_list)) #it returns the iterator so need to convert back to list
print(reversed_list_2)