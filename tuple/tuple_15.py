#15.How can you use tuples as dictionary keys?

#creating dict with tuple as keys:

my_dict={
    (1,2):'point a',
    (2,3):'point b',
    (3,6):'point c'
}

#accessing values using tuple keys:

print(my_dict[(1,2)])

#checking if a tuple key exist in the dictionary:

if (5,6) in my_dict:
    print("The point exist")
else:
    print('not present')