class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print(self.__class__.nome)


class Cliente(Pessoa):
    ...

class Aluno(Pessoa):

c1 = Cliente('oscar', 'galicia')
c1 = Aluno('Diveana', 'Fletes') 

