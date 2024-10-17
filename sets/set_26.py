#26.How do you perform set operations (union, intersection, etc.) on more than two sets?

set_a={1,2,3,4,5,6}
set_b={1,2,4,5,6}
set_c={2,3,5,6}

#union

union=set_a.union(set_b,set_c)
print(union)

#using | operator

union2=set_a|set_c|set_b
print(union2)