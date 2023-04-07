import json

from aula202 import FILE, Person

with open(FILE, 'r') as file:
    datas = json.load(file)
    print(datas)

p1 = Person(**datas[0])
p2 = Person(**datas[1])

print(p1.name, p1.age)
print(p2.name, p2.age)
