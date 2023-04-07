from dataclasses import dataclass
from typing import Tuple


@dataclass
class Pais:
    nombre: str
    capital: str
    habitantes: int
    coordenadas: tuple

    # def __repr__(self):
    #     return (f'Esta es un {self.__class__.__name__} llamado {self.nombre}')


pais = Pais('Venezuela', 'Caracas', 3000000, (5.1632955 - 69.4146705))
print(pais)
# print(f'{pais.capital} es la capital de {pais.nombre} y cuenta con {pais.habitantes} de habitantes')
