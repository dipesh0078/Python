#29. How would you find the longest consecutive sequence in a list of numbers? 

def longest_consecutive_sequence(nums):
    if not nums:  
        return []

    num_set = set(nums)  
    longest_sequence = []
    
    for num in nums:
        if num - 1 not in num_set:  
            current_num = num
            current_sequence = [current_num]

            while current_num + 1 in num_set: 
                current_num += 1
                current_sequence.append(current_num)

            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence

    return longest_sequence

my_list = [100, 4, 200, 1, 3, 2]
longest_sequence = longest_consecutive_sequence(my_list)
print(longest_sequence) 