#18. How would you create a new list that contains 
# only the unique elements from an existing list? 

my_list=[1,2,1,1,3,3,4,5,6,7]

#Using a Set
unique=list(set(my_list))
print(unique)

#using loop:

temp_unique=[]

for item in my_list:
    if item not in temp_unique:
        temp_unique.append(item)

print(temp_unique)