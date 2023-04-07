# Crear sistema bancario com clase cliente, banco y cuenta, mediante la
# la agregación cada cliente debe tener cuenta(s) y cada banco clientes
# el cliente debe tener un metodo para sumar la totalidad de los saldos de sus cuentas
# cada banco debe tener un metodo para sumar la totalidad de los saldos de los clientes

class Clientes:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.cuenta = []

    def añadir(self, cuenta):
        self.cuenta.append(cuenta)

    def total_saldo(self):
        total = 0
        for cuenta in self.cuenta:
            total += cuenta.saldo
        print(total)


class Cuenta:
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo
        self.cliente = None

    def añadir_cuenta(self, cliente):
        self.cliente = cliente
        cliente.añadir(self)


class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.saldos = []

    def anexar(self, cliente):
        for cuentas in cliente.cuenta:
            self.saldos.append(cuentas.saldo)

    def saldo_banco(self):
        total = 0
        for saldo in self.saldos:
            total += saldo
        return total


diveana = Clientes('diveana', 'Rua 4')
oscar = Clientes('Oscar', 'Rua do Pomar')
ahorro_oscar = Cuenta('0010', 2500)
cuenta_de_ahorro = Cuenta('0001', 1000)
cuenta_corriente = Cuenta('0002', 50)
nubank = Banco('Nubank')

ahorro_oscar.añadir_cuenta(oscar)
cuenta_de_ahorro.añadir_cuenta(diveana)
cuenta_corriente.añadir_cuenta(diveana)

nubank.anexar(diveana)
nubank.anexar(oscar)

print(nubank.saldo_banco())
