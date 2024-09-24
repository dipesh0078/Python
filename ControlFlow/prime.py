number=int(input("Enter the number: "))

if number>1:
    for i in range(2,int(number/2)):
        if(number%i==0):
            print(f'The number {number} is not a prime number')
            break
    else:
        print(f'The number {number} is prime number')
else:
    print(f"{number} is not valid")