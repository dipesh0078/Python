#9. Write a function is_prime(n) that checks if a number n is prime.

def is_prime(n):
    count=0
    for i in range(1,n+1):
        if (n%i==0):
            count+=1
    
    if count==2:
        return True
    else:
        return False
    

number=int(input('Enter your number: '))

print(is_prime(number))