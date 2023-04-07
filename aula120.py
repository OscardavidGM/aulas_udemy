from os import system

options = ["LIST", "UNDO", "REDO"]
to_do = []
lixo = []

while True:
    print("\n  What do you want to do: \n")
    DO = input("LIST, UNDO, REDO: ").upper()

    if DO not in options:
        print("Please, choose a valid option \n")
    if DO == "LIST":
        new_task = str(input("All right! Write a new task: "))
        to_do.append(new_task)
        print("\n", *to_do, sep=", \n")
    if DO == "UNDO":
        if len(to_do) > 0:
            novo_lixo = to_do.pop()
            lixo.append(novo_lixo)
            print("\n", *to_do, sep=", \n")
        else:
            print("There is nothing to UNDO \n")
            system('cls')
    if DO == "REDO":
        if len(lixo) > 0:
            to_do.append(lixo[-1])
            lixo.pop()
            print("\n", *to_do, sep=", \n")
        else:
            print("There is nothing to REDO \n")
            system('cls')
