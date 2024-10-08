#28. How would you check if one list is a subset of another list? 

list1=[1,2,3,4,5,6]

list2=[1,2,3]

for x in list2:
    if x not in list1:
        print('Not a subset')
        break

print("It is a subset")
