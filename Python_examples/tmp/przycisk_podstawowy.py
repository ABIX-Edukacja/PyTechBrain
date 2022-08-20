# Kod źródłowy dla lekcji: Podstawowy przycisk
# Autor: Adam Jurkiewicz, ABIX Edukacja https://pytechbrain.edu.pl
#
#
from PyTechBrain import *
from time import sleep
uklad = PyTechBrain()

while True:
    sleep(0.1)
    a = uklad.przycisk_lewy()

    if a:
        b=1
        uklad.sygnalizator_czerwony('on')
        uklad.sygnalizator_zielony('off')
    else:
        b=0
        uklad.sygnalizator_czerwony('off')
        uklad.sygnalizator_zielony('on')

    print( (a,b) )
