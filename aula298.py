import locale
import string
from datetime import datetime
from pathlib import Path

locale.setlocale(locale.LC_ALL, '')
CAMINHO = Path(__file__).parent / 'aula298.txt'


def converte_para_brl(numero: float | int) -> str:
    brl = 'R$ ' + locale.currency(val=numero, symbol=False, grouping=True)
    return brl


data = datetime(2023, 4, 1)
dados = dict(
    nome='João',
    valor=converte_para_brl(123456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O.G',
    telefone='+123455677'
)

# print(json.dumps(dados, indent=2, ensure_ascii=False))

with CAMINHO.open('r', encoding='UTF8') as arquivo:
    texto = arquivo.read()
    template = string.Template(texto)
    print(template.substitute(dados))
