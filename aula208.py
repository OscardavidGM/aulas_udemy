class Foo:
    def __init__(self):
        self.public = 'isso é publico'
        self._protected = 'isso é protegido'
        self.__exemplo = 'isso é privado'

    def metodo_publico(self):
        self.metodo_protected()
        print(self._protected)
        return 'metodo_publico'

    def metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'


f = Foo()
# print(f._protected)
# print(f.public)
print(f.metodo_publico())
