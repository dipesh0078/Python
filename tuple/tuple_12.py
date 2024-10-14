#12.How do you convert a tuple into a string?

my_tuple=(1,2,3,4,6,7)
string=''
for x in my_tuple:
    string=string+str(x)

print(string) 

#efficient method:

string2=''.join(str(x) for x in my_tuple)
print(string2)