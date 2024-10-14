#3. Write a function factorial(n) that returns the factorial of a given
#number n.

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

num=int(input('Enter your number: '))

print(fact(num))