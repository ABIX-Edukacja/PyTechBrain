# Kod źródłowy dla lekcji: Tęcza i dyskoteka - wersja z iteracją
# Autor: Adam Jurkiewicz, ABIX Edukacja https://pytechbrain.edu.pl
#
from PyTechBrain import *
from time import sleep
from random import randint
uklad = PyTechBrain()


while True:
    print('Zapalam czerwoną')
    for liczba in range(255):
        uklad.RGB_czerwona(liczba)
        sleep(0.02)

    print('Gaszę czerwoną')
    uklad.RGB_czerwona(0)

    print('Zapalam niebieską')
    for liczba in range(255):
        uklad.RGB_niebieska(liczba)
        sleep(0.02)

    print('Gaszę niebieską')
    uklad.RGB_niebieska(0)

    print('Zapalam zieloną')
    for liczba in range(255):
        uklad.RGB_zielona(liczba)
        sleep(0.02)

    print('Gaszę zieloną')
    uklad.RGB_zielona(0)

