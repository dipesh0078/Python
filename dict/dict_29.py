#29. How do you find the intersection of two dictionaries (keys that exist in both)?
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
intersection_keys = set(dict1.keys()) & set(dict2.keys())

print(intersection_keys)  