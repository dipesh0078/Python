#22.Write a recursive function fibonacci_recursive(n) to return the n-th
#Fibonacci number.

def fibonacci_recursive(n):
    if n<=1:
        return n
    else:
        return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)
    

print(fibonacci_recursive(7))

for i in range(7):
    print(fibonacci_recursive(i))