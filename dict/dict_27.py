#27. How do you nest dictionaries and access deeply nested values?

nested_dict = {
    'person': {
        'name': 'Alice',
        'age': 30,
        'address': {
            'street': '123 Main St',
            'city': 'New York',
            'zip': '10001'
        }
    },
    'job': {
        'title': 'Engineer',
        'company': 'Tech Corp'
    }
}


name = nested_dict['person']['name']
city = nested_dict['person']['address']['city']
job_title = nested_dict['job']['title']

print(name)      
print(city)     
print(job_title)  