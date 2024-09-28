n=int(input("Enter the range: "))

for i in range(n):
    for j in range(i+1):
        print(i+1,end='')
    print()
    
for i in range(n-1):
    for j in range(n-i-1):
        print(n-1-i, end='')
    print()