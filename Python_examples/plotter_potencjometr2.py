# Kod źródłowy dla lekcji: Plotter z potencjometru + dioda PWM
# Autor: Adam Jurkiewicz, ABIX Edukacja https://pytechbrain.edu.pl
#
from PyTechBrain import *
from time import sleep
uklad = PyTechBrain()

while True:
    sleep(0.1)
    a = uklad.potencjometr_raw()
    b = int( (a/1023) * 255)
    uklad.PWM_modulacja(b)
    print( (a,b) )


