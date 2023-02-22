# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

L1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
L2 = ['BA', 'SP', 'MG', 'RJ', 'RR']
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from itertools import zip_longest

def zipper(l1, l2):
    L3 = []
    menor = l1 if len(l1) <= len(l2) else l2

    for x in range(len(menor)):
        L3 += [(l1[x], l2[x])]
    return L3


# print(zipper(L1, L2), sep="\n")
# print(list(zip(L1, L2)))
print(list(zip_longest(L1, L2, fillvalue= "SEM CIDADE")))
