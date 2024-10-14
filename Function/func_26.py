#26.Write a recursive function power(x, n) that returns x raised to the power of n.

def power(x,n):
    if n==0:
        return 1
    else:
        return x*power(x,n-1)
    
print(power(2,4))