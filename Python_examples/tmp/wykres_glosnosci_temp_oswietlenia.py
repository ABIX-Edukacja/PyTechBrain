# Kod źródłowy dla lekcji: wykres danych z czujników
# Autor: Adam Jurkiewicz, ABIX Edukacja https://pytechbrain.edu.pl
#
from PyTechBrain import *
from time import sleep
uklad = PyTechBrain()

while True:
    sleep(0.1)
    temp = uklad.temperatura_C()
    osw = uklad.fotorezystor_raw()
    glos = uklad.glosnosc_raw()

    print( (temp, osw, glos) )