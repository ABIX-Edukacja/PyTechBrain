# Kod źródłowy dla lekcji:
# Kolory ustawiane przez przycisk + potencjometr - instrukcje warunkowe

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


print(
    """
Please move potentiometer while pressing button:

LEFT - RED | MIDDLE - GREEN | RIGHT - BLUE
"""
)

while True:

    sleep(0.1)
    change_red = my_board.get_left_button_state()
    change_green = my_board.get_middle_button_state()
    change_blue = my_board.get_right_button_state()

    # now we check, if any button pressed, if not, we break
    if not any((change_red, change_green, change_blue)):
        print("No one button pressed...")
        exit_application(0)

    new_value = int((my_board.get_potentiometer_raw() / 1023) * 255)

    if change_red:
        my_board.set_signal_red(new_value)

    elif change_green:
        my_board.set_signal_green(new_value)

    elif change_blue:
        my_board.set_signal_blue(new_value)
