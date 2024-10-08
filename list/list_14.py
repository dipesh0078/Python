#14. How can you access every second element in a list? 

my_list=[1,2,3,4,5,6,7,8]

second_elements=my_list[::2]

print(second_elements)

#my_list[::2] starts from the beginning of the list (default start is 0 and end is the end of the list) and 
# selects every second element by specifying a step of 2.