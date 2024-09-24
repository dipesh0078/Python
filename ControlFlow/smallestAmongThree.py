list=[]
list.append(int(input('Enter 1st number: ')))
list.append(int(input('Enter 2nd number: ')))
list.append(int(input('Enter 3rd number: ')))
temp=list[0]
for i in list:
    if(i<temp):
        temp=i

print(f' The smallest among {list} is {temp}')
