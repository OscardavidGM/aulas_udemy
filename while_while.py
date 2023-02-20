qtd_lineas = 5
qtd_columnas = 5

linea = 1
while linea <= qtd_lineas:
    columna = 1
    while columna <= qtd_columnas:
        print(f"{linea=} {columna=}")
        columna += 1
    linea += 1

print("Acabó!")        