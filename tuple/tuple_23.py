#23.How do you handle a tuple of unknown size when unpacking into variables?
#Unpacking with a wildcard (*)
my_tuple2=(1,2,3,4,5,6,7)

d,e,f,*rem=my_tuple2

print(d,e,f)
print(rem)