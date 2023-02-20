def numeros(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total

multiplica = numeros(1, 2, 3, 4)
print(multiplica)
