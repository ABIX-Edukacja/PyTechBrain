import pyfirmata

board = pyfirmata.Arduino("/dev/ttyACM0")

SENSOR_PIN = 0
LED_PIN = 13

it = pyfirmata.util.Iterator(board)
it.start()

board.analog[SENSOR_PIN].enable_reporting()

while True:
    light_level = board.analog[SENSOR_PIN].read()
    print "Reading from analog sensor: %s" % light_level
    board.pass_time(1)
    # EXERCISE add blinking of LEDs in response to reading
    # delay = ...
    # board.digital[LED_PIN].write(1)
    # board.pass_time(delay)
    # board.digital[LED_PIN].write(0)
    
