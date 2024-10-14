#23.Write a recursive function sum_digits(n) that returns the sum of the
#digits of a number.


def sum_digits(n):
    if n==0:
        return 0
    else:
        return n%10+sum_digits(n//10)
    

print(sum_digits(52))