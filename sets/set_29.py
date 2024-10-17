#29.How do you check if two sets are equal?

set_a = {1, 2, 3}
set_b = {3, 2, 1}
set_c = {1, 2, 4}


are_equal_ab = set_a == set_b  
print(f"set_a is equal to set_b: {are_equal_ab}")


are_equal_ac = set_a == set_c 
print(f"set_a is equal to set_c: {are_equal_ac}")