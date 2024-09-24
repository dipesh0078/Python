number=int(input('Enter any number: '))
temp=number
def fact(x):
    fact=1
    for i in range(1,x+1):
        fact=fact*i
    return fact
l=len(str(number))
len=int(l)
sum=0
while number!=0:
    sum=sum+fact(number%10)
    number=int(number/10)
    len-=1
    

if(sum==temp):
    print('The number is strong number')
else:
    print('Not a strong number')

