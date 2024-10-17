#13.How do you find the difference between two sets?

set_a={1,2,3,4,5}
set_b={1,2,3,8,9}

diff_AB=set_a.difference(set_b)
print(diff_AB)

#using - operator
diff_BA=set_b-set_a
print(diff_BA)