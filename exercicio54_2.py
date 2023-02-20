"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input("Digite su horario: ")

try:
    horas= int(hora)
    if horas <= 11:
       print("Buenos Dias!")
    elif horas <= 17:
       print("Buenas tardes!")
    elif horas <= 23:
       print("Buenas Noches!")   
    else:
        print("No conozco esa hora")
except:
    print("por favor digite solo numeros enteros")

