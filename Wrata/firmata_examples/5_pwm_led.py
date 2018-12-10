import pyfirmata

DELAY = 0.5
brightness = 0

board = pyfirmata.Arduino("/dev/ttyACM0")

led = board.get_pin('d:11:p')

# increase
for i in range(0, 10):
    brightness = brightness + 0.1
    print "Setting brightness to %s" % brightness
    led.write(brightness)
    board.pass_time(DELAY)

# decrease
for i in range(0, 10):
    print "Setting brightness to %s" % brightness
    led.write(brightness) 
    brightness = brightness - 0.1       
    board.pass_time(DELAY)

board.exit()