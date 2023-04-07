import json
import os

# from typing import TypedDict

# class Movie(TypedDict):
#     name: str
#     yeâr: int
#     rating: float
#     director: None | str


# file_json = ''' {
#     "name": "Mad Max",
#     "yeâr": 2032,
#     "rating": 9.2,
#     "director": null

# }
# '''
# filme: Movie = json.loads(file_json)
# pprint(filme['director'])
# print(filme['year'])

# new_json = json.dumps(filme, indent=2, ensure_ascii=False)

NOME_ARQUIVO = 'aula289_JSON.json'
CAMINHO_ABSOLUTO = os.path.abspath(
    os.path.join(os.path.dirname(__file__), NOME_ARQUIVO))

filme = {
    "name": "Mad Max",
    "yeâr": 2032,
    "rating": 9.2,
    "director": None
}

with open(CAMINHO_ABSOLUTO, 'w', encoding='UTF8') as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)

with open(CAMINHO_ABSOLUTO, 'r',  encoding='UTF8') as arquivo:
    nome_filme = json.load(arquivo)
    print(nome_filme)
