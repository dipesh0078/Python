#9. How do you check if one set is a superset of another set?

set_a={1,2,3,4,5,6}
set_b={1,2,3}

#using issuperset()

print(set_a.issuperset(set_b))

#using => operator:

print( set_a >= set_b)