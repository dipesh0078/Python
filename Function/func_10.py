#10.Write a function sum_list(lst) that takes a list of numbers and returns
#their sum.

def sum_list(lst):
    sum=0
    for i in lst:
        sum=sum+i

    return sum


numbers=[1,2,3,4,5,6,7,8]

print(sum_list(numbers))