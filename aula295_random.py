import random

r = random.randrange(10, 20, 2)
a = random.randint(10, 20)
f = random.uniform(20, 30)
nomes = ['Luis', 'Helena', 'Joana']
random.shuffle(nomes)

novos_nomes = random.sample(nomes, k=2)
nomes_novos = random.choices(nomes, k=2)
print(nomes_novos)
