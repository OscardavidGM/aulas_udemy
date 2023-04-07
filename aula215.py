class Repostero:
    def __init__(self, name):
        self.name = name
        self.ingredients = None

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        self._ingredients = ingredients


class IngredientesDeReposteria:
    def __init__(self, nome):
        self.nome = nome

    def dulces(self):
        return f'{self.nome} listo para el postre'


repostero = Repostero('Oscar')
azucar = IngredientesDeReposteria('azucar y harina')
material = IngredientesDeReposteria('batidora')
repostero.ingredients = material

print(azucar.dulces())
print(material.dulces())
print(repostero.ingredients.dulces())
