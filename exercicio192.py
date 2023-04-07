user = ''
tareas = []
tareas_anteriores = []

while True:
    print('Lista de Tareas')
    print('Comandos: [L]istar', '[D]esfazer', '[R]efazer')
    user = input('Digite una tarea o comando: ')

    if user == 'L':
        print(*tareas, sep='\n')

        for datos in tareas:
            print(datos)

    elif user == 'D':
        if tareas == []:
            print("nada para desfazer")
        else:
            tareas_anteriores.append(tareas[-1])
            tareas.pop()
            print("Tareas")

            for datos in tareas:
                print(datos)

    elif user == 'R':
        tareas.append(tareas_anteriores[-1])
        tareas_anteriores.pop()

        for datos in tareas:
            print(datos)
