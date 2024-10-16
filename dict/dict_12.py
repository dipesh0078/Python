#12. How do you merge two dictionaries?

dict1={'a':1,'b':2,'c':3}
dict2={'A':1,'B':2,'C':3}
#using merge operator
merged_dict=dict1|dict2
print(merged_dict)

#using update
dict1.update(dict2)
print(dict1)