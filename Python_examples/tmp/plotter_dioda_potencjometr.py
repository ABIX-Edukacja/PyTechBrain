# Kod źródłowy dla lekcji: Plotter oraz natężenie świecenia diody z potencjometru
# Autor: Adam Jurkiewicz, ABIX Edukacja https://pytechbrain.edu.pl 
#
from PyTechBrain import *
from time import sleep
uklad = PyTechBrain()

while True:
    a , b , c = uklad.fotorezystor_raw(), uklad.potencjometr_raw(), uklad.potencjometr_skala()
  
    print( ( a, b, c ) )
    uklad.PWM_modulacja(b)
    sleep(0.1)
    
    