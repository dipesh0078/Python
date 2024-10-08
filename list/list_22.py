#22. How would you check if a list is a palindrome? 

#using slicing:

list1=[1,2,3,4,5,6]
list2=[6,5,4,3,2,1]

if list1==list2[::-1]:
    print("The list are pallindrome")
else:
    print('The list are not pallindrome')