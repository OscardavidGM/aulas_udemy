from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('-b', '--basic')
args = parser.parse_args()

if args.basic is None:
    print('vocÊ não passou o valor de b.')
else:
    print('', args.b)
