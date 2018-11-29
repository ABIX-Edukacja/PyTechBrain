PyTechBrain - innowacyjna nauka programowania

Chciałbym przedstawić inspirację dla nauczycieli, w pełni zgodną z nową podstawą programową. To innowacyjny projekt - wprowadzający do tematu IoT. 
Łączy elektronikę i programowanie w jednym pudełku, pozwala uczyć od klasy 4 szkoły podstawowej do końca liceum. 
Zaczynamy środowiskiem opartym o Scratch, po czym przechodzimy do Pythona. Wszystko z czujnikami i diodami w tle...

PyTechBrain to nowa platforma wprowadzająca uczniów w dziedzinę IoT - Internet of Things (Internet Rzeczy). 
Pozwala na nauczanie elektroniki i programowania w jednym. Jest w pełni zgodna z nową Podstawą Programową. 
Łaczy prostotę wykonania i olbrzymie mozliwości nauczania programowania. Możemy wykorzystywać ją do budowania stacji pogodowych, podstaw inteligentnego miasta.  

Kompatybilny z Arduino UNO R3 i językiem Python

Pamiętaj - po podłączeniu zestawu USB do komputera standardowo urządzenie jest dostępne pod adresem /dev/ttyUSB0

Minimalny kod w Python:


from PyTechBrain import *
uklad = PyTechBrain()

====================================================================
Sterownik dla Windows: https://www.ftdichip.com/Drivers/VCP.htm
Oprogramowanie Graficznie : http://snap4arduino.rocks/
====================================================================
Przypisanie pinów:
# wejścia cyfrowe - przyciski
self.B01 = self.board.get_pin('d:12:i')
self.B02 = self.board.get_pin('d:11:i')
self.B03 = self.board.get_pin('d:10:i')
# wyjścia cyfrowe
self.L13 = self.board.get_pin('d:13:o')
# Dioda PWM
self.PWM = self.board.get_pin('d:9:p')
# Sygnalizator
self.L_R = self.board.get_pin('d:8:o')
self.L_Y = self.board.get_pin('d:7:o')
self.L_G = self.board.get_pin('d:2:o')
# dioda RGB
self.P_R = self.board.get_pin('d:5:p') 
self.P_G = self.board.get_pin('d:3:p')
self.P_B = self.board.get_pin('d:6:p')
# buzzer
self.BUZ = self.board.get_pin('d:4:o')
# czujniki analogowe
self.fotorezystor   = self.board.get_pin('a:2:i')
self.glosnosc       = self.board.get_pin('a:3:i')
self.temperatura    = self.board.get_pin('a:4:i')
self.potencjometr   = self.board.get_pin('a:5:i')

==============================================================
