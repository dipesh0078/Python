#9. How can you count the number of elements in a list? 

#we can count by using the len function :

my_list=[1,2,3,6,7,8,9,0,3]

print(len(my_list))

#we can use loop also :
count=0
for i in my_list:
    count+=1
print(count)