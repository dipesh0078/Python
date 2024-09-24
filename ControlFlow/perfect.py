number=int(input('Enter your number: '))
list=[]
for i in range(1,int(number)):
    if(number%i==0):
        list.append(i)
sum=0
print(list)
for x in list:
    sum=sum+x
print(sum)
if(number==sum):
    print(f'{number} is a Perfect number')
else:
    print(f'{number} is not a perfect number')
