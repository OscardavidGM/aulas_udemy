from aula225x import logFileMixin


class Eletrico:
    def __init__(self, name):
        self._name = name
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if self._ligado:
            self._ligado = False


class Smartphone(Eletrico, logFileMixin):
    def ligar(self):
        super().ligar()

        if self._ligado:
            msg = f'{self._name} está ligado'
            self.log_sucess(msg)

    def desligar(self):
        super().desligar()

        if not self._ligado:
            msg = f'{self._name} está desligado'
            self.log_error(msg)
