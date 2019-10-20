# Kod źródłowy dla lekcji: Podstawowy przycisk - alfabet morse'a
# Autor: Adam Jurkiewicz, ABIX Edukacja https://pytechbrain.edu.pl
#
#
from PyTechBrain import *
from time import sleep
uklad = PyTechBrain()

print('Lewy przycisk...')
while True:
    a = uklad.przycisk_lewy()

    if a:
        uklad.sygnalizator_czerwony('on')
    else:
        uklad.sygnalizator_czerwony('off')

