frase = "aaaaeeeiouuuuuuuuu"

i = 0
apareceu_mais = 0
cantidad_letra_atual = ""

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == " ":                                                                          
        i += 1
        continue  
    
    letra_apareceu_mais_atual = frase.count(letra_atual)

    if apareceu_mais < letra_apareceu_mais_atual:
        apareceu_mais = letra_apareceu_mais_atual
        cantidad_letra_atual = letra_atual
    i += 1

print(letra_apareceu_mais_atual, cantidad_letra_atual)