#37.Write a function print_details(**kwargs) that prints out all the key- value pairs passed as keyword arguments.

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_details(name="hari", age=30, city="ktm", occupation="Engineer")