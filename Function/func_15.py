#15.Write a function find_gcd(a, b) that returns the greatest common
#divisor of two numbers.

def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b  
    return a  


num1 = 48
num2 = 18
print(f"The GCD of {num1} and {num2} is: {find_gcd(num1, num2)}")