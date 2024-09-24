number=int(input("Enter your number: "))

match number%2:
    case 0:
        print(f"The number {number} is a even number ")
    case _:
        print(f'The number {number} is odd number')


