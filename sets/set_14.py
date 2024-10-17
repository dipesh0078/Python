#14.How do you find the symmetric difference of two sets?

set_a={1,2,3,4,5}
set_b={2,3,4}

#using symmetric_difference():

symm_diff=set_a.symmetric_difference(set_b)
print(symm_diff)

#using ^ operator

symm_diff2= set_a ^ set_b
print(symm_diff2)