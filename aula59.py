
from pathlib import Path

camino_proyecto = Path()
print(camino_proyecto.absolute())

camino_archivo = Path(__file__)
print(camino_archivo)

ideas = camino_archivo.parent / 'ideas'
# print(ideas / 'archivo.txt')

archivo = Path.home() / 'Desktop' / 'archivo.txt'
archivo.touch()
print(archivo)
archivo.write_text('Hola')
print(archivo.read_text())
