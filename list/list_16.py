#16. How would you remove all occurrences of a specific element from a list? 

my_list=[1,2,3,4,5,6,7,8,1,1,1]

element_remove=1
#using list compherension
new_list=[x for x in my_list if x!=element_remove]
print(new_list)

#Using a While Loop with remove()

while element_remove in my_list:
    my_list.remove(element_remove)

print(my_list)

my_list=[1,2,3,4,5,6,7,8,1,1,1]



