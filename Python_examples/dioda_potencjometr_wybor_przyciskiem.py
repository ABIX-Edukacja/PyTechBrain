# Kod źródłowy dla lekcji: Plotter z potencjometru + dioda PWM
# Autor: Adam Jurkiewicz, ABIX Edukacja https://pytechbrain.edu.pl
#
from PyTechBrain import *
from time import sleep
uklad = PyTechBrain()

print('Wybierz przycisk, a następnie kręć potencjometrem')
print('lewy = RED, środkowy = GREEN, prawy = BLUE')

while True:

    sleep(0.1)
    uklad.RGB_kolor(0,0,0)
    r = uklad.przycisk_lewy()
    g = uklad.przycisk_srodkowy()
    b = uklad.przycisk_prawy()

    if r:
        potencjometr = uklad.potencjometr_raw()
        b = int( (potencjometr/1023) * 255)
        uklad.RGB_czerwona(b)

    elif g:
        potencjometr = uklad.potencjometr_raw()
        b = int( (potencjometr/1023) * 255)
        uklad.RGB_zielona(b)

    elif b:
        potencjometr = uklad.potencjometr_raw()
        b = int( (potencjometr/1023) * 255)
        uklad.RGB_niebieska(b)

    else:
        pass