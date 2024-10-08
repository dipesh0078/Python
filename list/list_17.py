#17. Given two lists, how would you find the common elements between them? 

list1=[1,2,3,4]
list2=[1,5,3,2]

#Using List Comprehension

common_elements=[element for element in list1 if element in list2]
print(common_elements)

#Using Set Intersection
# Convert lists to sets and find the intersection
common_elements_2=list(set(list1)&set(list2))
print(common_elements_2)