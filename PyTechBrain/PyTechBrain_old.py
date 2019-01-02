try:
    from pyfirmata import *
except:
    print('Brak modułu PyFirmata - PyTechBrain nie będzie działać prawidłowo....')
    print('------------[ ERROR ]------------------------------------------------')

from time import sleep
import serial,sys
import serial.tools.list_ports

class PyTechBrain(object):
    '''
    Obiekt typu PyFirmata, kod działa z Python3 - płytka produkcji ABIX Edukacja
    Uwaga - na chwilę obecną automatyczne wyszukiwanie płytki działa w Linux i Windows (sprawdzone)
    wówczas szukaj  = 'auto' lub w ogóle nie trzeba nic podawać, w macOS należy  podac odpowiedni COM, np. /dev/cuayyy34
    chętnych do współtworzenia kodu zapraszamy
    wersja z ulepszoną obsługą wczytywania klawiszy
    '''



    def __init__(self,szukaj='auto'):
        def portArduino():
            lists = list(serial.tools.list_ports.comports())
            lists = sorted(lists)
            for x in lists:
                if x[1].find('FT231X') != -1:
                    return x
            return 'BRAK'

        if szukaj == 'auto':
            try:
                # self.board = util.get_the_board(base_dir='/dev/serial/by-id/', identifier='usb-')
                p = portArduino()
                port = p[0]
                print('OK - znaleziono PyTechBrain...'+port+' => '+p[2])
                self.board = Arduino(port)
            except:
                print('Coś nie tak z poszukiwaniem plytki - może nie podłączona lub to nie jest Linux? [port: '+port+' ]')
                raise
        else:
            try:
                self.board = Arduino(szukaj)
            except:
                print('Coś nie tak z poszukiwaniem plytki - może nie podłączona (MacOS) ?')
                raise


        # wejścia cyfrowe - przyciski
        self.B01 = self.board.get_pin('d:12:i')
        self.B01.enable_reporting()
        self.B02 = self.board.get_pin('d:11:i')
        self.B02.enable_reporting()
        self.B03 = self.board.get_pin('d:10:i')
        self.B03.enable_reporting()
        # wyjścia cyfrowe
        self.L13 = self.board.get_pin('d:13:o')
        # Dioda PWM
        self.PWM = self.board.get_pin('d:9:p')
        # Sygnalizator
        self.L_R = self.board.get_pin('d:8:o')
        self.L_Y = self.board.get_pin('d:7:o')
        self.L_G = self.board.get_pin('d:2:o')
        # dioda RGB
        self.P_R = self.board.get_pin('d:5:p') # sprawdzić !!!!
        self.P_G = self.board.get_pin('d:3:p')
        self.P_B = self.board.get_pin('d:6:p')
        # buzzer
        self.BUZ = self.board.get_pin('d:4:o')
        # czujniki analogowe
        #                   = self.board.get_pin('a:0:i')
        #                   = self.board.get_pin('a:1:i')
        self.fotorezystor   = self.board.get_pin('a:2:i')
        self.fotorezystor.enable_reporting()
        self.glosnosc       = self.board.get_pin('a:3:i')
        self.glosnosc.enable_reporting()
        self.temperatura    = self.board.get_pin('a:4:i')
        self.temperatura.enable_reporting()
        self.potencjometr   = self.board.get_pin('a:5:i')
        self.potencjometr.enable_reporting()
        # włączam raportowanie
        self.it = util.Iterator(self.board)
        self.it.start()

    def LED(dioda,stan):
        '''
        Niskopoziomowa funkcja - nie korzystaj z niej normalnie.
        '''
        if stan == 'on':
            dioda.write(1)
        if stan == 'off':
            dioda.write(0)

    def RGB_czerwona(self,nasilenie):
        '''
        nasilenie - wartość od 0 do 1 - odpowiada 0..255 w RGB
        '''
        if nasilenie < 0:
            nasilenie = 0
        if nasilenie > 1:
            nasilenie = 1
        self.P_R.write(nasilenie)

    def RGB_zielona(self,nasilenie):
        '''
        nasilenie - wartość od 0 do 1 - odpowiada 0..255 w RGB
        '''
        if nasilenie < 0:
            nasilenie = 0
        if nasilenie > 1:
            nasilenie = 1
        self.P_G.write(nasilenie)

    def RGB_niebieska(self,nasilenie):
        '''
        nasilenie - wartość od 0 do 1 - odpowiada 0..255 w RGB
        '''
        if nasilenie < 0:
            nasilenie = 0
        if nasilenie > 1:
            nasilenie = 1
        self.P_B.write(nasilenie)

    def RGB_kolor(self,red,green,blue):
        '''
        ta funkcja ustawi diodę RGB - podajemy wartości od 1 do 255,
        funkcja przeliczy resztę
        '''
        self.RGB_czerwona(red/255.0)
        self.RGB_zielona(green/255.0)
        self.RGB_niebieska(blue/255.0)

    def PWM_modulacja(self,nasilenie):
        '''
        nasilenie - wartość od 0 do 1 -
        '''
        if nasilenie < 0:
            nasilenie = 0
        if nasilenie > 1:
            nasilenie = 1
        self.PWM.write(nasilenie)

    def sygnalizator_czerwony(self,stan):
        '''
        stan = 'on' - włącza światło sygnalizatora
        stan = 'off' - wyłącza światło sygnalizatora
        '''
        if stan == 'on':
            self.L_R.write(1)

        if stan == 'off':
            self.L_R.write(0)

    def sygnalizator_zolty(self,stan):
        '''
        stan = 'on' - włącza światło sygnalizatora
        stan = 'off' - wyłącza światło sygnalizatora
        '''
        if stan == 'on':
            self.L_Y.write(1)

        if stan == 'off':
            self.L_Y.write(0)

    def sygnalizator_zielony(self,stan):
        '''
        stan = 'on' - włącza światło sygnalizatora
        stan = 'off' - wyłącza światło sygnalizatora
        '''
        if stan == 'on':
            self.L_G.write(1)

        if stan == 'off':
            self.L_G.write(0)

    def przycisk_left(self):
        for x in range(2):
            wynik = self.B01.read()
            if wynik:
                return wynik
        return wynik

    def przycisk_middle(self):
        for x in range(2):
            wynik = self.B02.read()
            if wynik:
                return wynik
        return wynik

    def przycisk_right(self):
        for x in range(2):
            wynik = self.B03.read()
            if wynik:
                return wynik
        return wynik

# poniżej stare wersje odczytu - nie zawsze działały jak należy
    def przycisk_lewy_old(self):
        wynik = self.B01.read()
        return 'HIGH' if wynik else 'LOW'

    def przycisk_srodkowy_old(self):
        wynik = self.B02.read()
        return 'HIGH' if wynik else 'LOW'

    def przycisk_prawy_old(self):
        wynik = self.B03.read()
        return 'HIGH' if wynik else 'LOW'
###############################################################


# metody odczytujące czujniki analogowe
    def temperatura_raw(self):
        '''
        zwraca wartość czujnika temperatury 'raw', czyli dokładnie od 0 do 1
        '''
        oddaj = self.temperatura.read()
        if oddaj == None:
            oddaj = 0
        return oddaj


    def temperatura_C(self):
        '''
        zwraca wartość czujnika temperatury przeliczoną na skalę Celcjusza
        Bazuje na scenariuszu E-SWOI (CC-BY-SA)
        http://e-swoi.pl/conspects/implementations/view/103/sterowanie-elementami-z-poziomu-aplikacji-s4a-pomiar-temperatury/
        '''
        x = self.temperatura_raw()
        wynik = round( ( ( (x*5) / 1024 ) - 0.05 ) / 0.01 )
        return wynik

    def fotorezystor_raw(self):
        '''
        zwraca wartość fotorezystora 'raw', czyli dokładnie od 0 do 1
        '''
        oddaj = self.fotorezystor.read()
        return 0 if oddaj == None else oddaj

    def glosnosc_raw(self):
        '''
        zwraca wartość czujnika głośności 'raw', czyli dokładnie od 0 do 1
        '''
        oddaj = self.glosnosc.read()
        return 0 if oddaj == None else oddaj

    def potencjometr_raw(self):
        '''
        zwraca wartość wychylenia potencjometru 'raw', czyli dokładnie od 0 do 1
        '''
        oddaj = self.potencjometr.read()
        return 0 if oddaj == None else oddaj


    def potencjometr_skala(self):
        '''
        zwraca wartość wychylenia potencjometru w skali od -50 do +50
        Zatem 0 to środek położenia potencjometru
        '''
        return ( self.potencjometr_raw() - 0.5 )

################################################################################


    def buzzer_sygnal(self):
        '''
        Aby wydobyć minimalny dźwięk, należy włączyć, wyłączyć i tak min. 2 razy
        '''
        for x in range(1):
            self.BUZ.write(1)
            sleep(0.06)
            self.BUZ.write(0)
            sleep(0.06)