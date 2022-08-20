# Kod źródłowy dla lekcji: Podstawowy przycisk - alfabet morse'a
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

print("Left button - red signal")
print("Right button - exit application")
while True:
    a = test_board.get_left_button_state(times=3)
    b = test_board.get_right_button_state(times=3)
    if b:
        print("Finish!")
        exit_application()
    if a:
        uklad.sygnalizator_czerwony('on')
    else:
        uklad.sygnalizator_czerwony('off')
