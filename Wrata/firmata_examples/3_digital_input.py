import pyfirmata

board = pyfirmata.Arduino("/dev/ttyUSB0)")

button = board.get_pin('d:2:i')

it = pyfirmata.util.Iterator(board)
it.start()

button.enable_reporting()

while True:
    if str(button.read()) == 'True':
        print "Pressed!"
    board.pass_time(1)