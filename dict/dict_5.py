#5. How do you remove a key-value pair from a dictionary?
my_dict={}
my_dict['name']='Dipesh'
my_dict['age']=23
my_dict['Address']='Gulmi'
print(my_dict)

#using pop() function
removed_value=my_dict.pop('age')
print(removed_value)
print(my_dict)

#using del keyword
del my_dict['Address']
print(my_dict)