pessoa = {}

chave = "nome"

pessoa[chave] = "Oscar"
pessoa["sobrenome"] = "Miranda"

print(pessoa[chave])

pessoa[chave] = "Maria"

del pessoa["sobrenome"]
print(pessoa)
print(pessoa["nome"])