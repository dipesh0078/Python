#21.Write a recursive function factorial_recursive(n) to find the factorial
#of a number.

def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)
    

result=factorial_recursive(5)
print(result)