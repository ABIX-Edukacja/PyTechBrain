import pyfirmata

LED_PIN = 13

# This is the port on the raspi, you will need to change this for Windows or Mac
# e.g. '\\.\COM3' for Windows or /dev/tty.usbmodemfa131' for Mac 
board = pyfirmata.Arduino("/dev/ttyACM0")

print "Running pyFirmata version:\t%s" % pyfirmata.__version__
print "Firmata version on board:\t%i.%i" % (board.get_firmata_version()[0], board.get_firmata_version()[1])

while True:
    board.digital[LED_PIN].write(0)
    board.pass_time(1)
    board.digital[LED_PIN].write(1)
    board.pass_time(1)

