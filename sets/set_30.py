#30.How do you use sets to solve a problem involving unique
#combinations or duplicates?

def unique_combinations(elements):
    unique_set=set()
    uniqe_elements=set(elements)
    for element1 in uniqe_elements:
        for element2 in uniqe_elements:
            if element1!=element2:
                unique_set.add(tuple(sorted((element1,element2))))
    
    return unique_set


    
input_list = [1, 2, 2, 3, 4]
unique_combinations = unique_combinations(input_list)

print(f"Unique pairs: {unique_combinations}")
    
    