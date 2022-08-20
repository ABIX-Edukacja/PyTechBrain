# Kod źródłowy dla lekcji: Tęcza i dyskoteka
# Autor: Adam Jurkiewicz, ABIX Edukacja https://pytechbrain.edu.pl
#
from PyTechBrain import *
from time import sleep
from random import randint
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

# now we do the rest.... because everything works!
while True:
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    my_board.set_rgb_color((red, green, blue))

    # wersja inna
    # new_color = (randint(0,255), randint(0,255), randint(0,255))
    # my_board.set_rgb_color(new_color)

    sleep(0.3)
