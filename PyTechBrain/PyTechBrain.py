'''
 Copyright (c) 2018 ABIX Edukacja - All rights reserved.
 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
 Version 3 as published by the Free Software Foundation; either
 or (at your option) any later version.
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.

 Program przeznaczony jest do płytki edukacyjnej PyTechBrain
 https://pytechbrain.edu.pl/
 https://sklep.cyfrowaszkola.waw.pl/PyTechBrain-Python-elektronika-mechatronika
 https://github.com/ABIX-Edukacja/PyTechBrain

 W programie wykorzystano moduł pymata_aio (https://github.com/MrYsLab/pymata-aio)
 autorstwa Alan'a Yorinks'a (MrYsLab) oraz oprogramowanie firmowe do Arduino tego
 autora (https://github.com/MrYsLab/pymata-aio/tree/master/FirmataPlus)
'''

_pytechbrain_version_ = '0.6a'

# definicje nut dla funkcji nuta
C0=16
Db0=17
D0=18
Eb0=19
E0=21
F0=22
Gb0=23
G0=24
Ab0=26
A0=27
Bb0=29
B0=31
C1=33
Db1=35
D1=37
Eb1=39
E1=41
F1=44
Gb1=46
G1=49
Ab1=52
A1=55
Bb1=58
B1=62
C2=65
Db2=69
D2=73
Eb2=78
E2=82
F2=87
Gb2=92
G2=98
Ab2=104
A2=110
Bb2=117
B2=123
C3=131
Db3=139
D3=147
Eb3=156
E3=165
F3=175
Gb3=185
G3=196
Ab3=208
A3=220
Bb3=233
B3=247
C4=262
Db4=277
D4=294
Eb4=311
E4=330
F4=349
Gb4=370
G4=392
Ab4=415
A4=440
Bb4=466
B4=494
C5=523
Db5=554
D5=587
Eb5=622
E5=659
F5=698
Gb5=740
G5=784
Ab5=831
A5=880
Bb5=932
B5=988
C6=1047
Db6=1109
D6=1175
Eb6=1245
E6=1319
F6=1397
Gb6=1480
G6=1568
Ab6=1661
A6=1760
Bb6=1865
B6=1976
C7=2093
Db7=2217
D7=2349
Eb7=2489
E7=2637
F7=2794
Gb7=2960
G7=3136
Ab7=3322
A7=3520
Bb7=3729
B7=3951
C8=4186
Db8=4435
D8=4699
Eb8=4978

# definicje czasów odgrywania nuta
#define BPM 120    //  you can change this value changing all the others
BPM=120
#define H 2*Q //half 2/4 and Q 60000/BPM //quarter 1/4
Q=60.0/BPM
H=2*Q
#define E Q/2   //eighth 1/8
E=Q/2
#define S Q/4 // sixteenth 1/16
S=Q/4
#define W 4*Q // whole 4/4
W=4*Q

try:
    from pymata_aio.pymata3 import PyMata3
    from pymata_aio.constants import Constants
    from sys import exit
except:
    print('Brak modułu PyMata3 - PyTechBrain nie będzie działać prawidłowo....')
    print('------------[ ERROR ]----------------------------------------------')

from time import sleep
# import serial
import serial.tools.list_ports

print('OK - załadowałem moduł PyTechBrain... [ '+ repr(_pytechbrain_version_) +' ]')

class PyTechBrain(object):
    '''
    Obiekt typu PyFirmata, kod działa z Python3 - płytka produkcji ABIX Edukacja
    Uwaga - na chwilę obecną automatyczne wyszukiwanie płytki działa w Linux i Windows (sprawdzone)
    wówczas szukaj  = 'auto' lub w ogóle nie trzeba nic podawać,
    w macOS być może też zadziała automat lub należy podać odpowiedni COM, np. szukaj='/dev/cuayyy34'
    chętnych do współtworzenia kodu zapraszamy https://github.com/ABIX-Edukacja/PyTechBrain
    '''



    def __init__(self,szukaj='auto'):
        def portArduino():
            lists = list(serial.tools.list_ports.comports())
            lists = sorted(lists)
            for x in lists:
                if x[1] == 'ABIX_PyTechBrain':
                    return x
            return None

        if szukaj == 'auto':
            print('Próba automatycznej detekcji portu ...')
            try:
                p = portArduino()
            except:
                print('Coś nie tak z poszukiwaniem plytki - może nie podłączona?')
                raise RuntimeError('Problem z automatyczną detekcją')
                exit()
            if p:
                port = p[0]
                print('OK - znaleziono PyTechBrain... ['+port+'] => '+p[2])
                self.board = PyMata3(com_port=port)
            else:
                print('Coś nie tak z poszukiwaniem plytki - może nie podłączona?')
                print('Parametr p => '+ str(p))
                raise RuntimeError('Problem z podłączeniem mimo znalezionego p.')
                exit()
        else:
            try:
                print('-------------[ ręcznie podany port ]-------------------------')
                print('Próba podłączenia portu podanego jako parametr...'+szukaj)
                self.board = PyMata3(com_port=szukaj)
            except:
                print('-------------[ ERROR ]-------------------------------------------------------')
                print('Coś nie tak z podłączeniem plytki do: '+szukaj+' - może nie podłączona ?')
                print('Spróbuj polecenia \"list_serial_ports\" wydanego w terminalu, np.: ')
                print('adasiek@adasiek-desktop:~$ list_serial_ports')
                print('/dev/ttyUSB0: FTDI')
                print('-------------[ ERROR ]-------------------------------------------------------')
                raise


        # ustawienie parametrów wejść/wyjść
        # wejścia cyfrowe - przyciski
        self.B01 = 12
        self.B02 = 11
        self.B03 = 10
        self.board.set_pin_mode(self.B01, Constants.INPUT)
        self.board.set_pin_mode(self.B02, Constants.INPUT)
        self.board.set_pin_mode(self.B03, Constants.INPUT)
        self.board.enable_digital_reporting(self.B01)
        self.board.enable_digital_reporting(self.B02)
        self.board.enable_digital_reporting(self.B03)
        # wyjścia cyfrowe LED serwisowy
        self.L13 = 13
        self.board.set_pin_mode(self.L13, Constants.OUTPUT)
        # Dioda PWM niebieska
        self.PWM = 9
        self.board.set_pin_mode(self.PWM, Constants.PWM)
        # Sygnalizator świateł na skrzyżowaniu
        self.L_R = 8  # red
        self.L_Y = 7  # yellow
        self.L_G = 2  # green
        self.board.set_pin_mode(self.L_R, Constants.OUTPUT)
        self.board.set_pin_mode(self.L_Y, Constants.OUTPUT)
        self.board.set_pin_mode(self.L_G, Constants.OUTPUT)
        # dioda RGB
        self.P_R = 5
        self.P_G = 3
        self.P_B = 6
        self.board.set_pin_mode(self.P_R, Constants.PWM)
        self.board.set_pin_mode(self.P_G, Constants.PWM)
        self.board.set_pin_mode(self.P_B, Constants.PWM)
        # buzzer
        self.BUZ = 4
        self.board.set_pin_mode(self.BUZ, Constants.OUTPUT)
        # czujniki analogowe
        #                   = 0
        #                   = 1
        self.FOTOREZYSTOR   = 2
        self.GLOSNOSC       = 3
        self.TEMPERATURA    = 4
        self.POTENCJOMETR   = 5
        self.board.set_pin_mode(self.FOTOREZYSTOR,  Constants.ANALOG)
        self.board.set_pin_mode(self.GLOSNOSC,      Constants.ANALOG)
        self.board.set_pin_mode(self.TEMPERATURA,   Constants.ANALOG)
        self.board.set_pin_mode(self.POTENCJOMETR,  Constants.ANALOG)
        self.board.enable_analog_reporting(self.FOTOREZYSTOR)
        self.board.enable_analog_reporting(self.GLOSNOSC)
        self.board.enable_analog_reporting(self.TEMPERATURA)
        self.board.enable_analog_reporting(self.POTENCJOMETR)
        # włączam raportowanie
        #self.it = util.Iterator(self.board)
        #self.it.start()

    def RGB_czerwona(self,nasilenie):
        '''
        nasilenie - wartość int 0..255
        '''
        if nasilenie < 0:
            nasilenie = 0
        if nasilenie > 255:
            nasilenie = 255
        self.board.analog_write(self.P_R, nasilenie)

    def RGB_zielona(self,nasilenie):
        '''
        nasilenie - wartość int 0..255
        '''
        if nasilenie < 0:
            nasilenie = 0
        if nasilenie > 255:
            nasilenie = 255
        self.board.analog_write(self.P_G, nasilenie)

    def RGB_niebieska(self,nasilenie):
        '''
        nasilenie - wartość int 0..255
        '''
        if nasilenie < 0:
            nasilenie = 0
        if nasilenie > 255:
            nasilenie = 255
        self.board.analog_write(self.P_B, nasilenie)

    def RGB_kolor(self,red,green,blue):
        '''
        ta funkcja ustawi diodę RGB - podajemy wartości int 0..255,
        wszystkie kolory w jednym parametrze (r,g,b) = Tupla
        '''
        self.RGB_czerwona(red)
        self.RGB_zielona(green)
        self.RGB_niebieska(blue)

    def PWM_modulacja(self,nasilenie):
        '''
        nasilenie - wartość int 0..255
        '''
        if nasilenie < 0:
            nasilenie = 0
        if nasilenie > 255:
            nasilenie = 255
        self.board.analog_write(self.PWM, nasilenie)

    def sygnalizator_czerwony(self,stan):
        '''
        stan = 'on' - włącza światło sygnalizatora
        stan = 'off' - wyłącza światło sygnalizatora
        '''
        if stan == 'on':
            self.board.digital_write(self.L_R,1)

        if stan == 'off':
            self.board.digital_write(self.L_R,0)

    def sygnalizator_zolty(self,stan):
        '''
        stan = 'on' - włącza światło sygnalizatora
        stan = 'off' - wyłącza światło sygnalizatora
        '''
        if stan == 'on':
            self.board.digital_write(self.L_Y,1)

        if stan == 'off':
            self.board.digital_write(self.L_Y,0)

    def sygnalizator_zielony(self,stan):
        '''
        stan = 'on' - włącza światło sygnalizatora
        stan = 'off' - wyłącza światło sygnalizatora
        '''
        if stan == 'on':
            self.board.digital_write(self.L_G,1)

        if stan == 'off':
            self.board.digital_write(self.L_G,0)

    def przycisk_lewy(self):
        '''
        zwraca True jeśli naciśnięty przycisk
        '''
        return self.board.digital_read(self.B01)

    def przycisk_srodkowy(self):
        '''
        zwraca True jeśli naciśnięty przycisk
        '''
        return self.board.digital_read(self.B02)

    def przycisk_prawy(self):
        '''
        zwraca True jeśli naciśnięty przycisk
        '''
        return self.board.digital_read(self.B03)

    # a teraz inna wersja, czyta dwa razy na wszelki wypadek
    def przycisk_lewy_2(self):
        '''
        zwraca True jeśli naciśnięty przycisk - dwa odczyty zanim zwróci wynik
        '''
        for x in range(2):
            wynik = self.board.digital_read(self.B01)
            if wynik:
                return wynik
        return wynik

    def przycisk_srodkowy_2(self):
        '''
        zwraca True jeśli naciśnięty przycisk - dwa odczyty zanim zwróci wynik
        '''
        for x in range(2):
            wynik = self.board.digital_read(self.B02)
            if wynik:
                return wynik
        return wynik

    def przycisk_prawy_2(self):
        '''
        zwraca True jeśli naciśnięty przycisk - dwa odczyty zanim zwróci wynik
        '''
        for x in range(2):
            wynik = self.board.digital_read(self.B03)
            if wynik:
                return wynik
        return wynik

    # metody odczytujące czujniki analogowe
    def temperatura_raw(self):
        '''
        zwraca wartość czujnika temperatury 'raw', czyli dokładnie co oddaje czujnik
        '''
        oddaj = self.board.analog_read(self.TEMPERATURA)
        return 0 if oddaj == None else oddaj

    def temperatura_C(self):
        '''
        zwraca wartość float temperaturę przeliczoną na skalę Celcjusza (99.9)
        Bazuje na obliczeniach ABIX
        '''
        x = self.temperatura_raw()
        wynik = float( round( ( x * 0.125 ) -  22 ,1 ) )
        return wynik

    def fotorezystor_raw(self):
        '''
        zwraca wartość fotorezystora 'raw', czyli dokładnie co oddaje czujnik
        '''
        oddaj = self.board.analog_read(self.FOTOREZYSTOR)
        return 0 if oddaj == None else oddaj

    def glosnosc_raw(self):
        '''
        zwraca wartość czujnika głośności 'raw', czyli dokładnie co oddaje czujnik
        '''
        oddaj = self.board.analog_read(self.GLOSNOSC)
        return 0 if oddaj == None else oddaj

    def potencjometr_raw(self):
        '''
        zwraca wartość wychylenia potencjometru 'raw', czyli dokładnie co oddaje czujnik
        '''
        oddaj = self.board.analog_read(self.POTENCJOMETR)
        return 0 if oddaj == None else oddaj


    def potencjometr_skala(self):
        '''
        zwraca wartość wychylenia potencjometru w skali od -52 do +51
        Zatem 0 to mniej więcej środek położenia potencjometru
        Ta funkcja wymaga zapewne doszlifowania ...
        '''
        return ( ( self.potencjometr_raw() - 511.5 ) // 10 )

################################################################################

    def nuta(self, f, t):
        '''
        Odgrywa nutę 'f' w czasie 't'
        Nuty zdefiniowane w bibliotece
        '''
        self.board.play_tone(4, Constants.TONE_TONE, f)
        sleep(t)
        self.board.play_tone(4, Constants.TONE_NO_TONE, f)

    def pauza(self, t):
        sleep(t)

    def graj_star_wars(self):
        self.nuta(A3,Q)
        self.nuta(A3,Q)
        self.nuta(A3,Q)
        self.nuta(F3,E+S)
        self.nuta(C4,S)
        self.nuta(A3,Q)
        self.nuta(F3,E+S)
        self.nuta(C4,S)
        self.nuta(A3,H)
        self.nuta(E4,Q)
        self.nuta(E4,Q)
        self.nuta(E4,Q)
        self.nuta(F4,E+S)
        self.nuta(C4,S)
        self.nuta(Ab3,Q)
        self.nuta(F3,E+S)
        self.nuta(C4,S)
        self.nuta(A3,H)
        self.nuta(A4,Q)
        self.nuta(A3,E+S)
        self.nuta(A3,S)
        self.nuta(A4,Q)
        self.nuta(Ab4,E+S)
        self.nuta(G4,S)
        self.nuta(Gb4,S)
        self.nuta(E4,S)
        self.nuta(F4,E)
        self.pauza(E)
        self.nuta(Bb3,E)
        self.nuta(Eb4,Q)
        self.nuta(D4,E+S)
        self.nuta(Db4,S)
        self.nuta(C4,S)
        self.nuta(B3,S)
        self.nuta(C4,E)
        self.pauza(1+E)
        self.nuta(F3,E)
        self.nuta(Ab3,Q)
        self.nuta(F3,E+S)
        self.nuta(A3,S)
        self.nuta(C4,Q)
        self.nuta(A3,E+S)
        self.nuta(C4,S)
        self.nuta(E4,H)
        self.nuta(A4,Q)
        self.nuta(A3,E+S)
        self.nuta(A3,S)
        self.nuta(A4,Q)
        self.nuta(Ab4,E+S)
        self.nuta(G4,S)
        self.nuta(Gb4,S)
        self.nuta(E4,S)
        self.nuta(F4,E)
        self.pauza(E)
        self.nuta(Eb4,Q)
        self.nuta(Bb3,E)
        self.nuta(D4,E+S)
        self.nuta(Db4,S)
        self.nuta(C4,S)
        self.nuta(B3,S)
        self.nuta(C4,E)
        self.pauza(E)
        self.nuta(F3,E)
        self.nuta(Ab3,Q)
        self.nuta(F3,E+S)
        self.nuta(C4,S)
        self.nuta(A3,Q)
        self.nuta(F3,E+S)
        self.nuta(C4,S)
        self.nuta(A3,H)
        self.pauza(2*H)

    def buzzer_sygnal(self,stan):
        '''
        stan = 'on' - włącza sygnał ciągły
        stan = 'off' - wyłącza sygnał ciągły
        stan = 'demo' - to do, demo muzyczki Star Wars - to do
        '''
        if stan == 'on':
            self.board.play_tone(4, Constants.TONE_TONE, 440)
        if stan == 'off':
            self.board.play_tone(4, Constants.TONE_NO_TONE, 440)
        if stan == 'demo':
            print('Demo - gramy Star Wars...')
            self.graj_star_wars()
