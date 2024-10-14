#16.How do you sort a list of tuples based on the second element in each tuple?

my_list=[(1,2),(3,4),(4,8),(6,9)]

sorted_list=sorted(my_list,key=lambda x:x[1])

print(sorted_list)