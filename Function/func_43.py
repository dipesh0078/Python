#43.Write a recursive function flatten_recursive(*args) that flattens any
#number of nested lists passed as arguments.

def flatten_recursive(*args):
    flattened = []  

    for item in args:
        if isinstance(item, list):  
            flattened.extend(flatten_recursive(*item))  
        else:
            flattened.append(item)  
            
    return flattened


result = flatten_recursive(1, [2, 3], [[4, 5], 6], 7, [8, [9, 10]])
print(result)  