# Kod źródłowy dla lekcji: Przyciski i światła
# Autor: Adam Jurkiewicz, ABIX Edukacja https://pytechbrain.edu.pl 

from PyTechBrain import *
from time import sleep
uklad = PyTechBrain()

while True:
    sleep(0.1)
    a,b,c = uklad.przycisk_left(), uklad.przycisk_middle(), uklad.przycisk_right()
    uklad.sygnalizator_czerwony('off')
    uklad.sygnalizator_zolty('off')
    uklad.sygnalizator_zielony('off')
    a1,b1,c1 = 0,0,0

    if a:
        a1 = 1
        uklad.sygnalizator_czerwony('on')
    elif b:
        b1 = 1
        uklad.11sygnalizator_zolty('on')
    elif c:
        c1 = 1
        uklad.sygnalizator_zielony('on')

    print( (a1, b1, c1) )
    