#21. How would you rotate a list by n positions to the left? 

def rotate_list(lst,n):
    n=n%len(lst)
    return lst[n:]+lst[:n]

my_list=[1,2,3,4,5,6,7,8]
rotated_list=rotate_list(my_list,3)
print(rotated_list)