"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self):
        self._name = None
        self._age = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value


class Customer(Person):
    def __init__(self):
        super().__init__()
        self.accounts = []

    def add(self, account):
        self.accounts.append(account)
        account.get_owner(self)


class Account(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

    def deposit(self, amount):
        self.balance += amount

    def get_owner(self, client):
        self.owner = client


class CheckingAccount(Account):
    def __init__(self, bank, agency: str, number: str, balance: float, extralimit=1000):
        self.agency = agency
        self.number = number
        self.balance = balance
        self.extralimit = extralimit
        self.owner = None
        self.bank = bank

    def withdraw(self, amount):
        if not self.bank.autentificacion(self.owner, self, self.agency):
            raise ValueError('Autentificacion failed')

        max_withdraw = self.balance - amount
        total_limit = -self.extralimit

        if max_withdraw >= total_limit:
            self.balance -= amount
        else:
            raise ValueError('Insufficent Balance')


class SavingsAccount(Account):
    def __init__(self, bank, agency, number, balance):
        self.agency = agency
        self.number = number
        self.balance = balance
        self.owner = None
        self.bank = bank

    def withdraw(self, amount):
        if not self.bank.autentificacion(self.owner, self, self.agency):
            raise ValueError('Autentificacion failed')

        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError('Insufficent Balance')


class Bank:
    def __init__(self):
        self.accounts = []
        self.clients = []

    def add_accounts(self, account):
        self.accounts.append(account)

    def add_customers(self, client):
        self.clients.append(client)

    def autentificacion(self, clients, account, agency):
        accounts = (c for c in self.accounts if c.agency ==
                    agency and c.owner == clients)
        return account in accounts


banesco = Bank()

diveana = Customer()
diveana.name = 'Diveana'
diveana.age = '28'

account1 = CheckingAccount(banesco, '0001', '23241', 1200)
account2 = SavingsAccount(banesco, '0002', '11111', 900)

diveana.add(account1)
diveana.add(account2)

banesco.add_accounts(account1)
banesco.add_accounts(account2)
banesco.add_customers(diveana)

account1.withdraw(300)
account2.withdraw(200)

for account in diveana.accounts:
    print(account.agency, account.balance)

account1.withdraw(1000)

for account in diveana.accounts:
    print(account.agency, account.balance)
