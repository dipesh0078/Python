#28. How do you invert a dictionary, i.e., swap keys and values?
my_dict = {'name': 'Alice', 'nickname': 'Alice', 'age': 25}

reversed_dict={value:key for key,value in my_dict.items()}
print(reversed_dict)