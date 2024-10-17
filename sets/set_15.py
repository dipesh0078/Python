#15.How do you remove duplicate elements from a list using a set?

lst=[1,2,2,2,1,1,1,4,5]

my_set=set(lst)
lst=list(my_set)
print(lst)
