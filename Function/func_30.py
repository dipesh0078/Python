#30.Write a lambda function to sort a list of tuples based on the second element.

sort_tuples= lambda lst: sorted(lst, key=lambda t:t[1])
tuples_list = [(1, 3), (2, 1), (4, 2), (3, 4)]
sorted_tuples = sort_tuples(tuples_list)
print(sorted_tuples) 