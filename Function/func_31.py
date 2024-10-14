#31.Write a lambda function to filter even numbers from a list.

filter_even=lambda lst: list(filter(lambda x: x%2==0, lst))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_even(numbers)

print(even_numbers)  