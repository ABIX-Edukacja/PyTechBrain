import pyfirmata
import random

board = pyfirmata.Arduino("/dev/ttyACM0")
RED_PIN = board.get_pin('d:9:p')
GREEN_PIN = board.get_pin('d:10:p')
BLUE_PIN = board.get_pin('d:11:p')

# light up red, green, blue
RED_PIN.write(1)
board.pass_time(0.5)
RED_PIN.write(0)
GREEN_PIN.write(1)
board.pass_time(0.5)
GREEN_PIN.write(0)
BLUE_PIN.write(1)
board.pass_time(0.5)

# randomly change colour every half second
while True:
    RED_PIN.write(random.random())
    GREEN_PIN.write(random.random())
    BLUE_PIN.write(random.random())
    board.pass_time(0.5)