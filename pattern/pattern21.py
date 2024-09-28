from math import factorial

n=int(input("Enter the number of rows: "))

for i in range(n):
    for j in range(1, n-i):
        print(' ', end='')
    for r in range(i+1):
        ncr=factorial(i)//(factorial(r)*factorial(i-r))
        print(ncr, end=' ')
    print()

