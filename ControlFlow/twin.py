print("Enter the range for twin number generation")
start=int(input("Start: "))
end=int(input('End: '))

def is_prime(n):
    for i in range(2, n):
        if(n%i==0):
            return False
    else:
        return True

for i in range(start,end):
    j=i+2
    if(is_prime(i) and is_prime(j)):
        print(f'({i},{j})\n')
    
