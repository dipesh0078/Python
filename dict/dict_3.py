#3. How do you access a value in a dictionary using its key?
my_dict={}

#adding a key-value pair:
my_dict['name']='Dipesh'
my_dict['age']=23
my_dict['Address']='Gulmi'

name_value=my_dict['name']
address_value=my_dict['Address']
print(name_value,address_value)

value = my_dict.get('happy', 'NaN')

print(value)
#If the key doesn't exist, it will return default_value 
# (or None if not specified) instead of raising an error.