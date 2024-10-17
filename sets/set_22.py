#22.How do you check if a set is a subset of another set using a set operation?

set_a = {1, 2}
set_b = {1, 2, 3, 4}


is_subset = set_a.difference(set_b) == set()

print(is_subset)  