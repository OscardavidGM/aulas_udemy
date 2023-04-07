import time

user = input('enter the time in seconds: ')

if user.isdigit():
    user = int(user)
else:
    print('invalid entry')
    quit()  # encierra ejecucion del programa

while user != 0:
    minutes, seconds = divmod(user, 60)  # retorna 2 cosas
    timer = '{:02d}:{:02d}'.format(minutes, seconds)
    print(timer, end='\r')
    time.sleep(1)
    user = user - 1


print('Time is up!!')
