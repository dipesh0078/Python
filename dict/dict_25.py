#25. How do you combine two dictionaries, summing values for common keys?
dict1={1:45,2:35,4:6}
dict2={1:3,2:5,7:45}

merged_dict={}

for key in dict1:
    merged_dict[key]=dict1[key]

for key in dict2:
    if key in merged_dict:
        merged_dict[key]+=dict2[key]
    else:
        merged_dict[key]=dict2[key]
print(merged_dict)