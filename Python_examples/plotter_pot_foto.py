# Kod źródłowy dla lekcji: Plotter z potencjometru + fotorezystora
# Autor: Adam Jurkiewicz, ABIX Edukacja https://pytechbrain.edu.pl
#
from PyTechBrain import *
from time import sleep
uklad = PyTechBrain()

while True:
    sleep(0.1)
    a = uklad.potencjometr_raw()
    b = uklad.fotorezystor_raw()
    print( (a,b) )


