n=5

for i in range(n):
    d=4-i
    c=0
    for j in range(i):
        print(' ',end='')
    for j in range(i,n):
        c=c+1
        print(c,end='')
    for j in range(n-i-1):
        print(d-j,end='')
    print()