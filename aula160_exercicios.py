# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

import copy

from dados import produtos

dict = [{**produto,'preco': round(produto['preco'] * 1.10, 2)} for produto in produtos]

# print(*dict, sep="\n")

dict2 = copy.deepcopy(dict)
# print(*dict2, sep="\n")


# dict2.sort(key=lambda perro: perro['preco'], reverse=False)

ape = sorted(dict2, key=lambda gato: gato['preco'], reverse=True)

print(*ape, sep="\n")
