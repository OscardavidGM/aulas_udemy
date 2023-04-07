class Car:
    def __init__(self, name):
        self.name = name
        self._engine = None
        self._maker = None

        @property
        def engine(self):
            return self._engine

        @engine.setter
        def engine(self, value):
            self._engine = value

        @property
        def maker(self):
            return self._maker

        @maker.setter
        def maker(self, value):
            self._maker = value


class Engine:
    def __init__(self, name):
        self.name = name


class Maker:
    def __init__(self, name):
        self.name = name


lincoln = Car('Lincoln')
ford = Maker('Ford')
engine = Engine('electric')
lincoln.maker = ford
lincoln.engine = engine

print(lincoln.name, lincoln.maker.name, lincoln.engine.name)
