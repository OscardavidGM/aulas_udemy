# import sys
from argparse import ArgumentParser

parser = ArgumentParser(description="Calcular area do retangulo")
# adicionar os argumentos

parser.add_argument(
    '-l', '--largura',
    type=int,
    help='largura do terreno',
    metavar='integer',
    default=10
)
parser.add_argument(
    '-c', '--comprimento',
    type=int,
    help='comprimento do terreno',
    metavar='integer',
    default=10
)

args = parser.parse_args()


def calcula_area(largura: int, comprimento: int):
    area = largura * comprimento
    return area


if __name__ == '__main__':
    print('A area do terreno é de %s m2' %
          calcula_area(args.largura, args.comprimento))
