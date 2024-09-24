number=int(input("Enter your number "))
temp=number
sum=0
i=0
while number!=0:
    digit=number%10
    sum=sum+digit*pow(10,i)
    number=int(number/10)
    i+=1
    

if(sum==temp):
    print(f'{temp} number is pallindrome')
else:
    print(f'{temp} is not a pallindrome')
