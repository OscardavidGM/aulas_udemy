with open('impares.txt', 'w') as impares, open('pares.txt', 'w') as pares:
    for n in range(0, 1000):
        if n % 2 == 0:
            pares.write(f'{n}\n')
        else:
            impares.write(f'{n}\n')

with open('Multiplos de 4.txt', 'w') as multiplos4:
    with open('pares.txt') as pares:
        for lines in pares.readlines():
            if int(lines) % 4 == 0:
                multiplos4.write(lines)
