#18.How do you nest tuples within another tuple, and how do you access nested elements?

nested_tuple = ((1, 2), (3, 4), (5, 6))


first_nested = nested_tuple[0]
print(first_nested) 
first_element = nested_tuple[0][0]
print(first_element)  
second_element = nested_tuple[1][1]
print(second_element)