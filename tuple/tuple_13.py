#13.How do you find the index of an element in a tuple?

my_tuple=(1,2,3,45,6,7,2)

print(my_tuple.index(7))

try:
    index = my_tuple.index(10)  # Element not in the tuple
    print(index)
except ValueError:
    print("Element not found in the tuple.")