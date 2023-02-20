"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = float(input("Digite un numero entero: "))

if numero % 2 == 0:
    print(f"El numero {numero} es par")
elif numero % 2 != 0 :
    print(f"El numero {numero} es impar")    
else:
    print("No digitaste un numero entero, intenta de nuevo")    

    