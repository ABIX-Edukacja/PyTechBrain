""" test with library newest version"""

from PyTechBrain import *
from time import sleep as s

test_board = PyTechBrain()
if test_board.board_init():
    print("Super!")
    test_board.set_buzzer("beep")  # demo, on, off
    print("f", test_board.get_fotoresistor_raw())
    print("p", test_board.get_potentiometer_scale())
    print("c", test_board.get_temperature_celcius())
    print("v", test_board.get_volume_sensor_raw())
    s(0.1)
    test_board.set_rgb_color((255, 255, 255))
    test_board.set_signal_red("on")
    test_board.set_signal_yellow("on")
    test_board.set_signal_green("on")
    test_board.set_pwm_diode(300)
    print("KONIEC")
    s(5)