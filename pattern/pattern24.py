n=5

for i in range(n):
    d=65+i
    for j in range(i):
        print(' ', end='')
    for j in range(n-i):
        print(chr(d+j), end='')
    for j in range(n-1-i):
        print(chr(68-j), end='')
    print()
