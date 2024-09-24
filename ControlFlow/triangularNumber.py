number=int(input("Enter a number to find its Triangular Number: "))
temp=number
sum=0

while number!=0:
    sum=sum+number
    number=number-1

print(f"The triangular number of {temp} is {sum}")