from PyTechBrain import *
from time import sleep
uklad = PyTechBrain()

while True:
    sleep(0.1)
    a = uklad.potencjometr_raw()
    b = uklad.fotorezystor_raw()
    c = uklad.temperatura_C()
    d = uklad.temperatura_raw()
    e = uklad.glosnosc_raw()
    print( (a,b,c,d,e ) )
    
    
    
    