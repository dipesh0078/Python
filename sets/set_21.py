#21.How do you find the Cartesian product of two sets?

set_a={1,2}
set_b={'a','b'}

cartesian_product=set()

for a in set_a:
    for b in set_b:
        cartesian_product.add((a,b))
    
print(cartesian_product)