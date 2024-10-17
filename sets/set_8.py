#8. How do you check if one set is a subset of another set?

set_a={1,2,3}
set_b={1,2,3,4,5}
set_c={2,1,0}
#using issubset() method:

print(set_a.issubset(set_b))

#using <= operator:
print(set_c<= set_b)