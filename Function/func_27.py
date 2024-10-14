#27.Write a recursive function flatten(lst) that flattens a nested list structure.

def flatten(lst):
    if not lst:
        return []
    elif isinstance(lst[0],list):
        return flatten(lst[0])+flatten(lst[1:])
    else:
        return[lst[0]]+flatten(lst[1:])
    

print(flatten([1, [2, [3, 4], 5], 6]))