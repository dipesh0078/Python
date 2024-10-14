#12.Write a function remove_duplicates(lst) that removes duplicate
#elements from a list.

def remove_duplicates(lst):
    temp=[]
    for i in lst:
        if i not in temp:
           temp.append(i)
    return temp

my_list = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(my_list))