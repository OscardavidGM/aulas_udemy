class Persona:
    def __init__(self):
        self._age = 0


@property
def age(self):
    print('getter aqui')
    return self._age


@age.setter
def age(self, a):
    if (a < 18):
        raise ValueError('no es criterio')
    print('setter aqui')
    self._age = a


persona = Persona()

persona.age = 19
print(persona.age)
