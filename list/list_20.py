#20. How would you split a list into two parts at a given index? 
#using slicing concept:

main_list=[1,2,3,4,5,6,7]
split_index=3

part_one=main_list[0:split_index]
part_two=main_list[split_index:]
print(part_one)
print(part_two)