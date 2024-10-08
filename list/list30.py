
def majority_element(nums):
    candidate = None
    count = 0

   
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    
    count = 0
    for num in nums:
        if num == candidate:
            count += 1

    if count > len(nums) // 2:
        return candidate
    else:
        return None 


my_list = [3, 2, 3]
majority = majority_element(my_list)
print(majority) 

my_list2 = [1, 2, 3, 4]
majority2 = majority_element(my_list2)
print(majority2)
