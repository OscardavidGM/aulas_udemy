import curses
import queue
import time
from curses import wrapper

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]


def print_maze(maze, stdscr, path=[]):  # 12
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j*2, "X", RED)
            else:
                stdscr.addstr(i, j*2, value, BLUE)


def find_start(maze, start):  # 3 recorremos el laberinto, pasamos por todas las lineas
    for i, row in enumerate(maze):
        for j, value in enumerate(row):  # pasamos x los valores de c/ linea
            if value == start:
                return i, j  # retornamos la posicion en que este

    return None


def find_path(maze, stdscr):  # 2 deter. la posicion inicial del laberinto
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    q = queue.Queue()  # 4 def. nuestra 1era estructura de datos
    # adicionamos la posicion inicial y puntos iniciales
    q.put((start_pos, [start_pos]))

    visited = set()  # 5 conjunto visitado acompañado con los elementos que visito

    while not q.empty():
        # 6 obtener la posicion actual y el camino = de lo que estuviera en frente de la fila
        current_pos, path = q.get()
        row, col = current_pos  # obtener la linea en la columna de la posicion actual

        stdscr.clear()  # 7 diseñar el laberinto con cualquier camino actual
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()

        if maze[row][col] == end:  # 8 verificar si esta en el final
            return path  # si esta en el fin retornar el camino, sino continua

        # 9 para encontrar vecinos en el laberinto y llamar
        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:  # recorrer todas las posiciones vecinas validas
            if neighbor in visited:  # verificar si son visitados
                continue

            r, c = neighbor  # 10 verificar si son un obstaculo, si lo son se ignora. sino -->
            if maze[r][c] == "#":
                continue

            # adicionarlo al camino y a la fila, xq hay que verificar si son el nudo final
            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)  # se adiciona al conjunto visitado


def find_neighbors(maze, row, col):  # 11
    neighbors = []

    if row > 0:  # UP
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):  # DOWN
        neighbors.append((row + 1, col))
    if col > 0:  # LEFT
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]):  # RIGHT
        neighbors.append((row, col + 1))

    return neighbors


def main(stdscr):  # 1
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(maze, stdscr)
    stdscr.getch()


wrapper(main)
