#22. How do you count the occurrences of each element in a list using a dictionary?

my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
count_dict={}
for item in my_list:
    if item in count_dict:
        count_dict[item]+=1
    else:
        count_dict[item]=1
print(count_dict)