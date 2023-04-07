# Class: Inheritance, Abstract Method, Class Method, Static Method, Agregação (Asociacion), tipagem
# Dataclass, __repr__, getter, setter

from abc import ABC, abstractmethod
from dataclasses import dataclass


class Person(ABC):
    def __init__(self, name: str, age: int, address: str = 'N/A') -> None:
        self.name = name
        self.age = age
        self._address = address
        assert self.age > 9 and isinstance(
            self.age, int), 'Your age needs to be greater than 9 years old'

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if isinstance(value, str):
            self._address = value
        else:
            raise ValueError("The value is no correct!")

    def __repr__(self) -> str:
        return f"Person {self.name!r}, {self.age}, {self.address!r}"

    @abstractmethod
    def run(self):
        return "Running!"


class Dog:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def bark(self):
        return 'Woof!'

    def __repr__(self) -> str:
        return f"Pet {self.name!r}, {self.age} years old"


class Client(Person):
    number = 0

    def __init__(self, name: str, age: int, pet: Dog, address: str = 'N/A',
                 profession: str = 'N/A') -> None:

        super().__init__(name, age, address)
        self.profession = profession
        self.pet = pet

    def __repr__(self) -> str:
        return f"Client {self.name!r}, {self.age}, {self.address!r}, {self.profession!r}"

    @staticmethod
    def complain():
        print('---- Contanding ----')

    @classmethod
    def count(cls):
        Client.complain()
        cls.number += 1
        return cls.number

    def run(self):
        return "Walking"


# @dataclass
# class Gato:
#     name = str
#     age = int


atenas = Dog('Atenas', 3)
# ladilla = Gato()

diveana = Client('Diveana', 28, atenas)
diveana.address = 'Rua do Pomar'
diveana.profession = 'Medic'

print(diveana)
print()
print(Client.count())
print()
print(diveana.pet.bark())
print(diveana.run())
