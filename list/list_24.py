#How would you find the second largest element in a list 
# without using built-in sorting functions? 

def find_second_largest(lst):
    if len(lst) < 2:
        return None  

    
    largest = second_largest = float('-inf')

    for num in lst:
        if num > largest:
            second_largest = largest 
            largest = num  
        elif num > second_largest and num != largest:
            second_largest = num  

    return second_largest if second_largest != float('-inf') else None


my_list = [3, 5, 1, 8, 7, 8]
second_largest = find_second_largest(my_list)
print(second_largest)