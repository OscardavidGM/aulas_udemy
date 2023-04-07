import csv
from pathlib import Path

CAMINHO = Path(__file__).parent / 'filecsv.csv'
CAMINHO.touch()
# print(CAMINHO.exists())
# print(CAMINHO.is_file())

clientele = [
    {'Name': 'Oscar', 'Age': 28},
    {'Name': 'Diveana', 'Age': 28},
    {'Name': 'Monica', 'Age': 19}
]

with CAMINHO.open('w', encoding='UTF8') as file:
    columns = clientele[0].keys()
    escritor = csv.writer(file)

    escritor.writerow(columns)

    for clients in clientele:
        escritor.writerow(clients.values())
