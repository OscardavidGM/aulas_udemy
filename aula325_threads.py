from threading import Thread
from time import sleep

# def tardar(texto, tempo):
#     sleep(tempo)
#     print(texto)


# t = Thread(target=tardar, args=("Demoracion", 3))
# t.start()

# t1 = Thread(target=tardar, args=("Demoracion", 2))
# t1.start()

# t2 = Thread(target=tardar, args=("Demoracion", 5))
# t2.start()

# for i in range(10):
#     print(i)
#     sleep(.5)

def tardar(texto, tempo):
    sleep(tempo)
    print(texto)


t = Thread(target=tardar, args=("Hola mundo", 5))
t.start()

# while t.is_alive():
#     print('Esperando a thread')
#     sleep(2)

print('Thread Acabou')
