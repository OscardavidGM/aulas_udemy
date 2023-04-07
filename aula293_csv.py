import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'test.csv'

# with CAMINHO_CSV.open('r', encoding='UTF8') as arquivo:
#     leitor = csv.reader(arquivo)

#     for linha in leitor:
#         print(linha)

with CAMINHO_CSV.open('r', encoding='UTF8') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha['Nome'])
