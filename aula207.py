class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
        self._cor = self.cor_tinta

    @property
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta

    @cor.setter
    def cor(self, valor):
        self._cor = valor


caneta = Caneta('Azul')
caneta.cor = 'Rosa'
print(caneta.cor)
