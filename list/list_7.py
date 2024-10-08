#7. How can you concatenate two lists? 

#Using '+' operator

list1=[1,2,3]
list2=[4,5,6]

concatenated_list=list1+list2
print(concatenated_list)


#using extend() method
#The extend() method modifies the original list by appending elements from another list.
list1.extend(list2)
print(list1)
# Using list unpacking (*):
list1=[1,2,3]
list_concatenated=[*list1,*list2]
print(list_concatenated)



