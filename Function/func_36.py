#36.Write a function multiply_all(*args) that multiplies all the numbers passed as arguments.

def multiply_all(*args):
    result=1
    for i in args:
        result=result*i
    return result

print(multiply_all(1,2,3,4,5))

print(1*2*3*4*5)