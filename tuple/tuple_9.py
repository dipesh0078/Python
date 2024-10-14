#9. How do you unpack values from a tuple into variables?

my_tuple1=(1,2,3)

#unpacking
a,b,c=my_tuple1

print(a,b,c)
#Unpacking with a wildcard (*)
my_tuple2=(1,2,3,4,5,6,7)

d,e,f,*rem=my_tuple2

print(d,e,f)
print(rem)