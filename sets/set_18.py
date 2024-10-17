#18.How do you iterate over the elements of a set?

my_set={1,2,3,4,5,6,7}

for element in my_set:
    print(element)

for index, element in enumerate(my_set):
    print(f'{index}:{element}')