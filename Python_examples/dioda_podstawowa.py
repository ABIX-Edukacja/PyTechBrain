# Kod źródłowy dla lekcji: 1 - podstawy świecenia diodą
# Autor: Adam Jurkiewicz, ABIX Edukacja https://pytechbrain.edu.pl
#
from PyTechBrain import *
from time import sleep
uklad = PyTechBrain()

while True:
    uklad.sygnalizator_czerwony('on')
    sleep(0.3)
    uklad.sygnalizator_zielony('on')
    sleep(0.2)
    uklad.sygnalizator_zolty('on')
    sleep(0.7)
    uklad.sygnalizator_czerwony('off')
    sleep(0.4)
    uklad.sygnalizator_zielony('off')
    sleep(0.3)
    uklad.sygnalizator_zolty('off')
    sleep(0.3)