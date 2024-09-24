number=int(input("Enter your Number: "))
n1,n2=0,1

for i in range(2,number):
    n3=n1+n2
    n1=n2
    n2=n3
    print(f'{n3}\t', end='')