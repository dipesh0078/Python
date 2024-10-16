#10. How do you convert two lists (keys and values) into a dictionary?

key_lst=['name','Age','Address','Car']
value_lst=['Dipesh','20','Kathmandu','Nano']

#using zip() function
my_dict=dict(zip(key_lst,value_lst))
print(my_dict)