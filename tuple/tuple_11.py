#11.How do you iterate over a tuple?

my_tuple=(1,2,3,4,5,6)

for x in my_tuple:
    print(x)

#You can also use the enumerate() function if you want to access both the index 
# and the element while iterating:

for index, element in enumerate(my_tuple):
    print(f'Index {index}:{element}')