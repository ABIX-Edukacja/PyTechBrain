# Kod źródłowy dla lekcji:
# Tęcza budowana z kolorów RGB - pętla for i pętla nieskończona - pełna gama kolorów

# Autor: Adam Jurkiewicz, ABIX Edukacja https://pytechbrain.edu.pl
#
# template file to be used with PyTechBrain library
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

# now we do the rest.... because everything works!
while True:
    print("RED on...")
    for liczba in range(255):
        my_board.set_rgb_red(liczba)
        sleep(0.02)

    print("RED off...")
    my_board.set_rgb_red(0)

    print("GREEN on...")
    for liczba in range(255):
        my_board.set_rgb_green(liczba)
        sleep(0.02)

    print("GREEN off...")
    my_board.set_rgb_green(0)

    print("BLUE on...")
    for liczba in range(255):
        my_board.set_rgb_blue(liczba)
        sleep(0.02)

    print("BLUE off...")
    my_board.set_rgb_blue(0)
