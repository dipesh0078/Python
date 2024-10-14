#7. Write a function fibonacci(n) that returns the first n numbers in the
#Fibonacci sequence.

def fibonacci(n):
    seq=[0,1]
    if n<0:
        print('Invalid input')

    elif n==0:
        return [0]
    elif n==1 :
        return seq[:1]
   
    for i in range(2,n+1):
        next_number=seq[-1]+seq[-2]
        seq.append(next_number)
    return seq

num=int(input('Enter the nth number: '))

print(fibonacci(num))


