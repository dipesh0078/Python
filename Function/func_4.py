#4. Write a function find_max(a, b, c) that returns the largest of three
#numbers.

def find_max(a,b,c):
    if (a>=b) and (a>=c):
        return a
    elif (b>=c) and (b>=a):
        return b
    else:
        return c
    

a=4
b=7
c=11

print(find_max(a,b,c))