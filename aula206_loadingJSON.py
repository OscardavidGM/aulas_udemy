import json

from aula203_classes import ferrari, road

data = None
with open(road, 'r') as file:
    data = json.load(file)
    print(data)

print(data)
