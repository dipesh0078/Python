#27.How do you find all unique subsets of a given set?

def find_subsets(s):
    subsets=[set()]

    for element in s:
        new_subsets=[]
        for subset in subsets:
            new_subset=subset|{element}
            new_subsets.append(new_subset)
        subsets.extend(new_subsets)
    return subsets

my_set={1,2,3}
unique_subsets=find_subsets(my_set)
print(unique_subsets)


