number=int(input("Enter your Number: "))
check=int(input("Enter a number to check: "))
n1,n2=0,1
list=[]
for i in range(2,number):
    n3=n1+n2
    n1=n2
    n2=n3
    list.append(n3)

if check in list:
    print(f"{check} belong to the fibonacci series of {number}")
else:
    print(f"{check} doesn't belong to the fibonacci series of {number}")
