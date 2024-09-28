n=5

for i in range(n):
    d=64+i
    for j in range(1,n-i):
        print(' ', end=' ')
    for j in range(i+1):
        print(chr(65+j),end=' ')
    for j in range(i):
        print(chr(d-j),end=' ')
    print()