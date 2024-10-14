#22.How do you perform element-wise addition of two tuples of the same length?

my_tuple1=(1,2,3,4,5,6)
my_tuple2=(7,8,9,10,11,12)
final=tuple()
for x in range(len(my_tuple1)):
      final+=(my_tuple1[x]+my_tuple2[x],)

print(final)