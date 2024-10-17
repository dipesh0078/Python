#25.How do you remove multiple elements from a set at once?

set_a={1,2,3,4,5}

lst=[2,3]

#using difference_update
set_a.difference_update(lst)
print(set_a)

#using -= operator

set_b= {1, 2, 3, 4, 5}
lst = [2, 3]

set_b -= set(lst)  
print(set_a) 