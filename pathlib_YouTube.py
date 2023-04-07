# Para mexer com caminhos em sistemas operacionais

from pathlib import Path

caminho_projeto = Path()

# print(caminho_projeto)
# print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
# print(caminho_arquivo.parent / 'arquivo.txt')

arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
# arquivo.touch()
# arquivo.write_text("Hola, como estas mi amor?, buenos dias")
# print(arquivo.read_text())

arquivo.write_text('')
with arquivo.open('a+') as file:
    file.write('Hola, mi amor \n')
    file.write('Como estas?')

# print(arquivo.read_text())
arquivo.unlink()

pasta_nova = Path.home() / 'Desktop' / 'nova_pasta'
pasta_nova.mkdir(exist_ok=True)

subpasta = pasta_nova / 'subpasta'
subpasta.mkdir(exist_ok=True)

outro_arquivo = subpasta / 'arquivo 100.txt'
outro_arquivo.touch()
with outro_arquivo.open('w') as outro:
    outro.write("Mi amorsote bello")


caminho_files = Path.home() / 'Desktop' / 'nova_pasta'
files = caminho_files / 'files'
files.mkdir(exist_ok=True)

# for i in range(5):
#     file = files / f'arquivo_{i}.txt'
#     file.touch()
