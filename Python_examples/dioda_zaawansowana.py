# Kod źródłowy dla lekcji: 1 - podstawy świecenia diodą + losowanie
# Autor: Adam Jurkiewicz, ABIX Edukacja https://pytechbrain.edu.pl
#
from PyTechBrain import *
from time import sleep
from random import randint
uklad = PyTechBrain()



while True:
    sleep(0.4)
    liczba = randint(1,3)
    if liczba == 1:
        uklad.sygnalizator_czerwony('on')
        sleep(0.2)
        uklad.sygnalizator_czerwony('off')
    elif liczba == 2:
        uklad.sygnalizator_zielony('on')
        sleep(0.2)
        uklad.sygnalizator_zielony('off')
    else:
        uklad.sygnalizator_zolty('on')
        sleep(0.2)
        uklad.sygnalizator_zolty('off')