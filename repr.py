import os
import shutil
from itertools import count

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'Exemplo')
NOVA_PASTA = os.path.join(DESKTOP, 'Nova')

os.makedirs(NOVA_PASTA, exist_ok=True)

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    print(root)

# caminho = os.path.join('C:/users', 'Cliente', 'Documents', 'Diveana Documentos')

# # print(caminho)
# # print(os.path.exists(caminho))

# contador = count()

# for root, dirs, files in os.walk(caminho):
#     the_counter = next(contador)
#     print(the_counter, 'Pasta', root)

#     for dir_ in dirs:
#         camiho_completo = os.path.join(root, dir_)
#         os.unlink(camiho_completo)
