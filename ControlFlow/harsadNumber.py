number=int(input('Enter a number: '))
sum=0
temp=number
while number!=0:
    sum=sum+number%10
    number=int(number/10)
   

if(temp%sum==0):
    print(f'{temp} is a Harshad Number')
else:
    print(f'{temp} is not a Harshad Number')
