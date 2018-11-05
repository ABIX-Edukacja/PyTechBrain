from pyfirmata import *
from time import sleep as slp

class PyTechBrain(object):
    '''
    Obiekt typu PyFirmata, kod działa z Python3 - płytka produkcji ABIX Edukacja
    Uwaga - na chwilę obecną automatyczne wyszukiwanie płytki działa tylko w systemie Linux
    wówczas szukaj  = 'linux-auto'
    W systemie tym nie trzeba w ogóle podawać adresu, kod odnajdzie go poprzez funkcję szukającą
    w Windows lub macOS należy  podac odpowiedni COM, np. COM3, /dev/cuayyy34
    chętnych do współtworzenia kodu zapraszamy
    '''

    def __init__(self,szukaj):
        if szukaj == 'linux-auto':
            try:
                self.board = util.get_the_board(base_dir='/dev/serial/by-id/', identifier='usb-')
                for i in range(6):
                    self.board.digital[13].write(1)
                    slp(i/3)
                    self.board.digital[13].write(0)
                    slp(i/3)

            except:
                print('Coś nie tak z poszukiwaniem plytki - może nie podłączona lub to nie jest Linux?')
        else:
            try:
                self.board = Arduino(szukaj)
            except:
                print('Coś nie tak z poszukiwaniem plytki - może nie podłączona (Win/MacOS) ?')


        # wejścia cyfrowe - przyciski
        self.B01 = self.board.get_pin('d:12:i')
        self.B02 = self.board.get_pin('d:11:i')
        self.B03 = self.board.get_pin('d:10:i')
        # wyjścia cyfrowe
        self.L13 = self.board.get_pin('d:13:o')
        self.PWM = self.board.get_pin('d:9:p')
        self.L_R = self.board.get_pin('d:8:o')
        self.L_Y = self.board.get_pin('d:7:o')
        self.L_G = self.board.get_pin('d:2:o')
        self.P_R = self.board.get_pin('d:5:p') # sprawdzić !!!!
        self.P_G = self.board.get_pin('d:3:p')
        self.P_B = self.board.get_pin('d:6:p')
        self.BUZ = self.board.get_pin('d:4:o')
        # czujniki analogowe

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
