# Kod źródłowy dla lekcji:
# Plotter z potencjometru + dioda PWM

# Autor: Adam Jurkiewicz, ABIX Edukacja https://pytechbrain.edu.pl
#

from PyTechBrain import *
from time import sleep
from sys import exit as exit_application

# create object
my_board = PyTechBrain()

if my_board.board_init():  # initializing connection
    print("Super! Initialization complete.")
    my_board.set_buzzer("beep")  # demo, on, off
else:
    print("Something was wrong!")
    my_board.full_debug_output()
    my_board.usage_info()
    exit_application(2)

# we set off all outputs
if not my_board.set_off_outputs():
    print("Something was wrong!")
    my_board.full_debug_output()
    exit_application(2)


print("Please move potentiometer:")

while True:
    sleep(0.1)
    potentiometer_value = my_board.get_potentiometer_raw()
    new_value = int((potentiometer_value / 1023) * 255)
    my_board.set_pwm_diode(new_value)
