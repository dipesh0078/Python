#21. How do you create a dictionary with default values for missing keys?
from collections import defaultdict

my_dict=defaultdict(int)

my_dict['apple'] = 5
my_dict['banana'] = 3
print(my_dict['car'])