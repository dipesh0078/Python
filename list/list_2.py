#2. How do  you add an element to a list using indexing? 

my_list=[1,2,3]

my_list[2]=4 #this can only replace an element at a given index but cannot insert

#to insert element in a particular index we have
my_list.insert(3,15) 
#if the index value is gereater then the next possible index value then it will append it to the next possible index

print(my_list)