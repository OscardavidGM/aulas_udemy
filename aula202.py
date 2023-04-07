import json

FILE = "aula202.json"


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.age = surname


p1 = Person('Oscar', 'Galicia')
p2 = Person('Diveana', 'Fletes')
data = [vars(p1), vars(p2)]

with open(FILE, 'w') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)
