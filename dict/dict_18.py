#18. How do you find the key with the maximum value in a dictionary?
my_dict={1:'A',45:'G',7:'D',42:'T'}

max_key=max(my_dict,key=my_dict.get)
print(max_key)