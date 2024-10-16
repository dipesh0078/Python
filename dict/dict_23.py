#23. How do you group a list of items by a certain property using a dictionary?

people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 25},
    {'name': 'David', 'age': 30},
    {'name': 'Eve', 'age': 35}
]


grouped_by_age = {}


for person in people:
    age = person['age'] 
    if age not in grouped_by_age:
        grouped_by_age[age] = []  
    grouped_by_age[age].append(person)  

print(grouped_by_age)