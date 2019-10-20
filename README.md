**PyTechBrain - innowacyjna nauka programowania**

Chciałbym przedstawić inspirację dla nauczycieli, w pełni zgodną z nową podstawą programową. To innowacyjny projekt - wprowadzający do tematu IoT.
Łączy elektronikę i programowanie w jednym pudełku, pozwala uczyć od klasy 4 szkoły podstawowej do końca liceum.
Zaczynamy środowiskiem opartym o Scratch, po czym przechodzimy do Pythona. Wszystko z czujnikami i diodami w tle...

PyTechBrain to nowa platforma wprowadzająca uczniów w dziedzinę IoT - Internet of Things (Internet Rzeczy).
Pozwala na nauczanie elektroniki i programowania w jednym. Jest w pełni zgodna z nową Podstawą Programową.
Łaczy prostotę wykonania i olbrzymie mozliwości nauczania programowania. Możemy wykorzystywać ją do budowania stacji pogodowych, podstaw inteligentnego miasta.  

Kompatybilny z Arduino UNO R3 i językiem Python

Pamiętaj - po podłączeniu zestawu USB do komputera standardowo urządzenie jest dostępne pod adresem /dev/ttyUSB0

Minimalny kod w Python:

<code>
from PyTechBrain import *
uklad = PyTechBrain()
</code>
====================================================================

Sterownik dla Windows: https://www.ftdichip.com/Drivers/VCP.htm

Oprogramowanie Graficznie :

- Scratch 2.0 offline - https://scratch.mit.edu/download
- s2aio - https://pypi.org/project/s2aio/

====================================================================

Przypisanie pinów:

# wejścia cyfrowe - przyciski

self.B01 = 12

self.B02 = 11

self.B03 = 10

# wyjścia cyfrowe - dioda serwisowa

self.L13 = 13

# Dioda PWM

self.PWM = 9

# Sygnalizator świateł na skrzyżowaniu

self.L_R = 8

self.L_Y = 7

self.L_G = 2

# dioda RGB

self.P_R = 5

self.P_G = 3

self.P_B = 6

# buzzer sterowany tonowo

self.BUZ = 4

# czujniki analogowe

self.fotorezystor   = 2

self.glosnosc       = 3

self.temperatura    = 4

self.potencjometr   = 5

==============================================================

W programie wykorzystano moduł pymata_aio (https://github.com/MrYsLab/pymata-aio) autorstwa Alan'a Yorinks'a (MrYsLab) oraz oprogramowanie firmowe do Arduino tego autora (https://github.com/MrYsLab/pymata-aio/tree/master/FirmataPlus).
