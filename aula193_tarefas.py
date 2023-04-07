import json
from os import system


def read(tarefas, road):
    data = []
    try:
        with open(road, 'r', encoding='utf8') as field:
            data = json.load(field)
    except FileNotFoundError:
        print("This file does not exist")
        save(tarefas, road)
    return data


def save(tarefas, road):
    data = tarefas
    with open(road, 'w', encoding='utf8') as field:
        data = json.dump(tarefas, field, indent=2, ensure_ascii=False)
    return data


options = ["LIST", "UNDO", "REDO", "STOP"]
ROAD = 'tarefas.json'

tarefas = read([], ROAD)
lixo = []

while True:
    print("\n  What do you want to do: \n")
    DO = input("LIST, UNDO, REDO: ").upper().strip()

    if DO not in options:
        print("Please, choose a valid option \n")
    if DO == "LIST":
        new_task = str(input("All right! Write a new task: "))
        tarefas.append(new_task)
        print("\t", *tarefas, sep="\n")
    if DO == "UNDO":
        if len(tarefas) > 0:
            novo_lixo = tarefas.pop()
            lixo.append(novo_lixo)
            print("\t", *tarefas, sep="\n")
        else:
            print("There is nothing to UNDO \n")
            system('cls')
    if DO == "REDO":
        if len(lixo) > 0:
            tarefas.append(lixo[-1])
            lixo.pop()
            print("\t", *tarefas, sep="\n")
        else:
            print("There is nothing to REDO \n")
            system('cls')
    if DO == "STOP":
        break
    save(tarefas, ROAD)
