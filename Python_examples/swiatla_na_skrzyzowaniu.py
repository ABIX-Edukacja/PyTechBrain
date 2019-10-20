# Kod źródłowy dla lekcji: Światła na skrzyżowaniu
# Autor: Adam Jurkiewicz, ABIX Edukacja https://pytechbrain.edu.pl
#
from PyTechBrain import *
from time import sleep
uklad = PyTechBrain()

# na początku gasimy wszystkie światła
uklad.sygnalizator_czerwony('off')
uklad.sygnalizator_zolty('off')
uklad.sygnalizator_zielony('off')

while True:
    #zapala się czerwone
    uklad.sygnalizator_czerwony('on')
    sleep(1.7)
    uklad.sygnalizator_zolty('on')
    sleep(1.3)
    uklad.sygnalizator_czerwony('off')
    uklad.sygnalizator_zolty('off')
    uklad.sygnalizator_zielony('on')
    sleep(2.5)
    uklad.sygnalizator_zielony('off')
    uklad.sygnalizator_zolty('on')
    sleep(1.4)
    uklad.sygnalizator_zolty('off')

