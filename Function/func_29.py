#29.Write a lambda function that takes a list of numbers and returns a list of their squares.


square_list=lambda lst:[x**2 for x in lst]

numbers = [1, 2, 3, 4, 5]
squares = square_list(numbers)
print(squares) 