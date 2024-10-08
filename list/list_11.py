#11. How can you remove an element from a list by index? 

#By using pop() method:

my_list=[1,2,3,4,5,6,7]
my_list.pop(0) #it retruns the removed elements which can be assigned to another variable
print(my_list)


#using del statement:
#he del statement can be used to remove 
# an element at a specific index without returning it.
del my_list[0]
print(my_list)