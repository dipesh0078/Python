#25. How would you find pairs of elements in a 
# list that sum up to a specific number? 
def find_pairs(lst, target_sum):
    
    pairs = []    

    for number in lst:
        complement = target_sum - number  
        if complement in lst: 
            pairs.append((complement, number)) 
        

    return pairs  

my_list = [1, 2, 3, 4, 5]
print(find_pairs(my_list, 6))

              
