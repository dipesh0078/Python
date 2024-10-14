#14.Write a function sort_list(lst) that sorts a list of numbers in ascending
#order.

def sort_list(lst):
    n=len(lst)

    for i in range(n):
        for j in range(0,n-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]

my_list = [3, 1, 4, 1, 5, 9, 2, 6]
sort_list(my_list)
print(my_list)