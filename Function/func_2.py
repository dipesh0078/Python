#2. Write a function is_even(n) that returns True if a number is even, and
#False otherwise.

def is_even(n):
    if (n%2==0):
        return True
    else:
        return False
    

num=int(input('Enter your number: '))

print(is_even(num))