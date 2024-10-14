#39.Write a function describe_person(name, **kwargs) where name is a
#required argument, and other details like age, job, and city are
#optional keyword arguments.

def describe_person(name,**kwargs):
    print(f'{name} details are')
    for key,value in kwargs.items():
        print(f'{key}:{value}')
    return

name="Sajan"

details={'age':12,'address':'Ktm', 'Hobby':'Sleeping' }

describe_person(name,**details)