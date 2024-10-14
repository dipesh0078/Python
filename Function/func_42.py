#42.Write a recursive function sum_all_recursive(*args) that sums all
#numbers passed as arguments (including nested tuples or lists).

def sum_all_recursive(*args):
    total = 0  

    for item in args:
        if isinstance(item, (list, tuple)): 
            total += sum_all_recursive(*item)  
        elif isinstance(item, (int, float)):  
            total += item  
            
    return total


result = sum_all_recursive(1, 2, [3, 4], (5, 6, [7, 8]), 9)
print(result)  