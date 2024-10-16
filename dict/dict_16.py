#16. How do you get the value for a key without raising an error if the key doesn'texist?
my_dict={'A':1,'B':2}

value=my_dict.get('Random',True)
if value:
    print("The desired key is not present")