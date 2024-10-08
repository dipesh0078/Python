#13. How do you check if a list is empty? 

#using the len() function:

my_list=[]

if len(my_list)==0:
    print("The list is empty")
else:
    print('The list is not empty')

#Using not operator:

if not my_list:
    print("The list is empty")
else:
    print("The list is not empty")

#Direct comparison

if my_list==[]:
    print('The list is empty')
else:
    print('The list is not empty')