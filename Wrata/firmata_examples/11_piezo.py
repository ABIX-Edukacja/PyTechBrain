import pyfirmata
import math

board = pyfirmata.Arduino("/dev/ttyACM0")

# connect piezo to pin 9 to use PWM
SENSOR_PIN = 0
PIEZO_PIN = board.get_pin('d:9:p')

it = pyfirmata.util.Iterator(board)
it.start()

board.analog[SENSOR_PIN].enable_reporting()

# check buzzer is working
PIEZO_PIN.write(0.2)
board.pass_time(0.5)
PIEZO_PIN.write(0.6)
board.pass_time(0.5)
PIEZO_PIN.write(0.8)
board.pass_time(0.5)
PIEZO_PIN.write(0)

while True:
    light_level = board.analog[SENSOR_PIN].read()
    if (light_level != None):
        # you may wish to adjust the raw reading here to get a better range of beeps
        buzzer_value = light_level
        print "setting piezo to %s" % buzzer_value
        PIEZO_PIN.write(buzzer_value)
        board.pass_time(0.5)
        PIEZO_PIN.write(0)
        board.pass_time(0.5)
