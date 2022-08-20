# Kod źródłowy dla lekcji:
# Alfabet Morse'a: lewy klawisz kropka (czerwona dioda), środkowy klawisz kreska (zielony)
# Autor: Adam Jurkiewicz, ABIX Edukacja https://pytechbrain.edu.pl
#
#
# template file to be used with PyTechBrain library
from PyTechBrain import *
from time import sleep
from sys import exit as exit_application

# create object
test_board = PyTechBrain()

if test_board.board_init():  # initializing connection
    print("Super! Initialization complete.")
    test_board.set_buzzer("beep")  # demo, on, off
else:
    print("Something was wrong!")
    test_board.full_debug_output()
    test_board.usage_info()
    exit_application(2)

# now we do the rest....

print(
    """
Please press buttons:

LEFT - RED - dot | MIDDLE - GREEN - dash
"""
)

while True:
    dot = test_board.get_left_button_state(times=3)
    dash = test_board.get_right_button_state(times=3)

    if dot:
        my_board.set_signal_green("off")
        my_board.set_signal_red("on")
    elif dash:
        my_board.set_signal_red("off")
        my_board.set_signal_green("on")
