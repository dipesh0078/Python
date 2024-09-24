number=int(input("Enter your number: "))
temp=number
len=len(str(number))
sum=0
while number!=0:
    sum=sum+pow(number%10,len)
    number=int(number/10)

if (sum==temp):
    print(f'{temp} is a Armstrong Number')
else:
    print(f'{temp} is not a Armstrong number')
