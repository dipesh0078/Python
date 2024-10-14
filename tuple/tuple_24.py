#24.How would you implement a tuple as an immutable list and handle operations like appending?


def append_to_tuple(original_tuple, item):
    
    return original_tuple + (item,)


def create_immutable_list(elements):
    if not isinstance(elements, tuple):
        raise ValueError("Elements must be a tuple.")
    return elements


immutable_list = create_immutable_list((1, 2, 3))


new_immutable_list = append_to_tuple(immutable_list, 4)

print("Original Immutable List:", immutable_list)       
print("New Immutable List after appending 4:", new_immutable_list) 


print("Length of New Immutable List:", len(new_immutable_list))  


print("First Element:", new_immutable_list[0])  
print("Contains 2?", 2 in new_immutable_list)  