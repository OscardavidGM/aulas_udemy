lista = []


while True:
    usuario = input("Selecione una opción: \n [i]nsertar, [e]liminar, [l]istar ")
    if usuario == "l":
        print(lista)
    elif len(lista) == 0:
         print("No existe nada en la lista")
    
    if usuario == "i":
        valor = input("Valor: ")
        lista.append(valor)
        continue

    elif usuario == "e":
      if len(lista) > 0:
            escolha = lista.pop(0)
    apagar = int(input("Selecciona un indice a eliminar: "))  
    print(apagar)
    print(escolha)

    for i, e in enumerate(lista):
     print(f"{i}, {e}")
       











