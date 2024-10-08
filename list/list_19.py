#19. How would you flatten a list of lists into a single list (without using any built-in functions)? 
my_list=[1,2,3,4,['A','B','C'],['x','y','z']]
flattened_list=[]
for sublist in my_list:
    if isinstance(sublist,list):
     for element in sublist:
        flattened_list.append(element)
    else:
       flattened_list.append(sublist)

print(flattened_list)
