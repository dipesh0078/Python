#16.Write a function sum_of_squares(n) that returns the sum of squares
#of the first n natural numbers.

def sum_of_squares(n):
    result=n*(n+1)*(2*n+1)/6
    return result


number=int(input('Enter your number: '))

print(sum_of_squares(number))