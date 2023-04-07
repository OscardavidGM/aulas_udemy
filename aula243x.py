def add_repr(cls):
    def repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = repr
    return cls


@add_repr
class Team:
    def __init__(self, name):
        self.name = name


@add_repr
class Planet:
    def __init__(self, name):
        self.name = name


team1 = Team('Portugal')
team2 = Team('Brasil')
planet1 = Planet('Jupyter')
planet2 = Planet('Venus')

print(team1)
print(team2)
print(planet1)
print(planet2)
