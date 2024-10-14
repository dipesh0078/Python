#41.Write a function find_max_in_args(*args) that returns the maximum
#value from the arguments passed.

def find_max_args(*args):
    temp=0
    for i in args:
        if i>temp:
            temp=i
    return temp

print(find_max_args(1,2,3,4,51,2122,4))