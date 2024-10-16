#17. How do you reverse the key-value pairs in a dictionary?

my_dict = {'name': 'Alice', 'nickname': 'Alice', 'age': 25}

reversed_dict={value:key for key,value in my_dict.items()}
print(reversed_dict)