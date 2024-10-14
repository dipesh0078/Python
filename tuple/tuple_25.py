#25.How can you use a generator to create a tuple?
'''
You can use a generator expression to create a tuple in Python by
 passing the generator directly to the tuple() constructor. 
 This allows you to generate elements on-the-fly and create a 
tuple without storing all the elements in memory at once.'''


squared_tuple=tuple(x**2 for x in range(10))
print(squared_tuple)