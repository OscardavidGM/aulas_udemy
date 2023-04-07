# road = 'C:\\Users\\Cliente\\Documents\\projeto\\venv\\'

import os

road = 'test.txt'

with open(road, 'w+', encoding="utf-8") as newField:
    # print(type(newField))
    newField.write("Me conformo \n")
    newField.writelines(
        ("Mejorando \n", "Esto \n")
    )
    newField.writelines(
        ("Improving \n", "Atenção \n")
    )
    newField.seek(0, 0)
    print(*newField.readlines(), end="")

os.rename(road, 'test-aula189.txt')

# with open(road, 'r') as newField:
#     print(newField.read())
