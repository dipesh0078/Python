#26. How do you use a dictionary to simulate a switch-case statement?

def case_a():
    return 'Case A is triggered'
def case_b():
    return 'CAse B is triggered'
def case_c():
    return 'Case C is triggered'

switch={
    'A':case_a,
    'B':case_b,
    'C':case_c}

choice='C'

result=switch.get(choice,'Invalid')()
print(result)