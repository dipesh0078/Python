n=5
for i in range(n):
    d=i+1
    for j in range(i,n):
        print(' ',end='')
    for j in range(i+1):
        print(j+1,end='')
    for j in range(i):
        d=d-1
        print(d,end='')
    print()