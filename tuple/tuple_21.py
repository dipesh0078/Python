#21.How do you find the length of the longest tuple in a list of tuples?

my_tuple=(1,2,3,(2,3,4,5),(1,2,3),4,5)
l=0
for x in my_tuple:
    if isinstance(x,tuple):
        if len(x)>l:
            l=len(x)

print(l)
