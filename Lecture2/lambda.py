people = [
    {"name" : "Harry", "house" : "gryffindor"},
    {"name": "Choo", "house" : "ravenclaw"},
    {"name" : "Draco", "house" : "slytherin"}
]

"""
custom sorting basesd on house:
def f(person):
    return person["house"]
people.sort(key = f)
"""

#custom sorting using lambda function
people.sort(key = lambda person : person["name"])

print(people)