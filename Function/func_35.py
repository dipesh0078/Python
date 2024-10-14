#35.Write a function sum_all(*args) that takes any number of arguments and returns their sum.

def sum_all(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum

print(sum_all(1,2,3,4,5,6))

print(1+2+3+4+5+6)