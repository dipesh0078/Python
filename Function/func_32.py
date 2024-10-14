#32.Write a lambda function that finds the maximum of two numbers.

max_num= lambda x,y: x if x>y else y

num1 = 5
num2 = 10
maximum = max_num(num1, num2)

print(maximum) 