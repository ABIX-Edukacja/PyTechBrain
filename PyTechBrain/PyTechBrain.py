from pyfirmata import *

class PyTechBrain(object):


    def __init__(self):
        self = util.get_the_board(base_dir='/dev/serial/by-id/', identifier='usb-')
        self.PWM = self.get_pin('d:9:p')
        self.L_R = self.get_pin('d:5:o')

    def red(self,stan):
        if stan == 'on':
            self.L_R.write(1)
