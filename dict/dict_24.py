#24. How do you remove multiple keys from a dictionary at once?
my_dict = {'name': 'Ram', 'age': 25, 'city': 'New York', 'occupation': 'Engineer'}


keys_to_remove = ['age', 'city']


for key in keys_to_remove:
    my_dict.pop(key, None)  

print(my_dict)