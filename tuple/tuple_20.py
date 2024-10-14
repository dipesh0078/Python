#20.How do you check if a tuple contains other tuples as elements?

my_tuple=(1,2,(3,4))

for x in my_tuple:
    if isinstance(x,tuple):
        print(x,"It is a tuple")