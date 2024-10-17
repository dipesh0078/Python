#20.How do you find common elements between multiple sets?
#using intersection

set_a={1,2,3,4}
set_b={1,2,6,8}

intersection=set_a.intersection(set_b)
print(intersection)

#using & operator

common=set_a & set_b
print(common)