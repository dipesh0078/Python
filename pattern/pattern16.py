n=5

for i in range(n):
    d=0
    for j in range(i):
        print(' ',end='')
    for j in range(i,n):
        d=d+1
        print(d, end='')
    print()