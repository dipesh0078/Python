#13.Write a function merge_two_lists(lst1, lst2) that merges two lists into
#one.

def merge_two_lists(lst1,lst2):
    for i in lst2:
        lst1.append(i)
    return lst1

lst1=[1,2,3,4]
lst2=[5,6,7,8]

print(merge_two_lists(lst1,lst2))