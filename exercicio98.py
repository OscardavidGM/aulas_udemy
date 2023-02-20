
cpf_recibido= str(input("Digite su cpf "))
cpf = []
suma1 = 0
resto1 = 0




for i in cpf_recibido:
    cpf.append(int(i))

for i in range(0,9):
    digito_1 = cpf[i] * (10 - i)
    suma1 = suma1 + digito_1
    resto1 = suma1 % 11
    pdv = 0 if resto1 <= 9 else (11 - resto1)

if (cpf[9] == pdv):
    print("cpf valido")
else:
    print("Cpf invalido")