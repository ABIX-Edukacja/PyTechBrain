# Kod źródłowy dla lekcji: Podstawowy przycisk - alfabet morse'a
# Autor: Adam Jurkiewicz, ABIX Edukacja https://pytechbrain.edu.pl
#
#
from PyTechBrain import *
from time import sleep
uklad = PyTechBrain()

print('Przycisk...')
while True:
    l = uklad.przycisk_lewy()
    s = uklad.przycisk_srodkowy()
    p = uklad.przycisk_prawy()

    if l:
        uklad.sygnalizator_czerwony('on')
    else:
        uklad.sygnalizator_czerwony('off')

    if s:
        uklad.sygnalizator_zolty('on')
    else:
        uklad.sygnalizator_zolty('off')

    if p:
        uklad.sygnalizator_zielony('on')
    else:
        uklad.sygnalizator_zielony('off')


