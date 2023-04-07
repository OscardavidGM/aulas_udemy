import json


def file_json(name, object):
    with open(name, 'w', encoding='utf8') as file:
        json.dump(object.__dict__, file, indent=2, ensure_ascii=False)


road = 'ferrari.json'


class FastCar:

    def __init__(self, name, faster, engine=False):
        self.name = name
        self.faster = faster
        self.engine = engine

    def turn_on(self):
        if self.engine:
            return "The engine is already on"
        self.engine = True
        return "Turning on the engine"

    def speed_car(self):
        if self.engine:
            return f"{self.faster}!! How fast!"
        return "You need to turn on the Engine first"

    def turn_off(self):
        if self.engine:
            self.engine = False
            return "Turning off the engine"
        return "The engine is already off"


ferrari = FastCar('Ferrari', 200)
ferrari.__dict__['Colour'] = "Red"
mazda = FastCar('Mazda', 170)

file_json(road, ferrari)
