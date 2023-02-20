
while True:
    numero_1 = input("digite um numero:  ")
    numero_2 = input("digite outro numero:  ")
    operador = input("digite uma operação (+-*/):  ")

    numeros_validos = None

    num_1 = 0
    num_2 = 0

    try:
        num_1 = float(numero_1)
        num_2 = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
        
        if numeros_validos == None:
             print("Tem alguma parada errada nesses numeros, tenta de novo")
             continue
        
    operadores_validos = "*+-/"

    if len(operador) > 1:
        print("digite apenas um operador")
        continue
    
    if operador not in operadores_validos:
        print("Coloque um operador valido")
        continue

    print("Realizando tua conta:")

    if operador == "+":
        print(f"{num_1} + {num_2} = {num_1 + num_2}")

    elif operador == "-":
        print(f"{num_1} - {num_2} = {num_1 - num_2}")

    elif operador == "*":
        print(f"{num_1} * {num_2} = {num_1 * num_2}")

    elif operador == "/":
        print(f"{num_1} / {num_2} = {num_1 / num_2}")
    else:
        print("Doidera!")

    sair = input("Deseja sair do programa, escrevaa [S]:  ").lower().startswith("s")

    if sair is True:
        print("Obrigado por usar a calculadora")
        break