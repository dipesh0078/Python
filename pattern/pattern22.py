rows=int(input("Enter the number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print(chr(64+i+1), end=' ')
    print()