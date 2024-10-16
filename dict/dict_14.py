#14. How do you sort a dictionary by its keys?

dict1={1:'A',2:'B',45:'R',23:'G'}

sorted_keys=sorted(dict1.keys())

#create a new dictionary with sorted keys
sorted_dict=dict(sorted(dict1.items(),key=lambda item:item[0]))


print(sorted_dict)