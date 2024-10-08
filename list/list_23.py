#23. How would you sort a list without using any
#  built-in sort functions (e.g., using a sorting algorithm like bubble sort)? 

def sort(lst):
    n=len(lst)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
                swapped=True
        if not swapped:
            break
    return lst  

my_list=[1,3,5,7,8,9,4,3]
print(sort(my_list))
            
          

