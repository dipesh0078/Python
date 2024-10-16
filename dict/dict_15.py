#15. How do you sort a dictionary by its values?

my_dict = {'banana': 3, 'apple': 5, 'orange': 2}

sorted_dict=dict(sorted(my_dict.items(),key=lambda item:item[1]))
print(sorted_dict)