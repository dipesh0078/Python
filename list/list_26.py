#26. How would you remove duplicates from a list while preserving the original order?

def remove_duplicates(lst):
    seen=set()
    unique_lst=[]
    for x in lst:
        if x not in seen:
            seen.add(x)
            unique_lst.append(x)
    return unique_lst

my_list=[1,2,2,2,3,4,2,5]
print(remove_duplicates(my_list))