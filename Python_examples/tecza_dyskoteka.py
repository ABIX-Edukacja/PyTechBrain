# Kod źródłowy dla lekcji: Tęcza i dyskoteka
# Autor: Adam Jurkiewicz, ABIX Edukacja https://pytechbrain.edu.pl
#
from PyTechBrain import *
from time import sleep
from random import randint
uklad = PyTechBrain()


while True:
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    uklad.RGB_kolor(r, g, b)
    sleep(0.2)