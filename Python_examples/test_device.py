# template file to be used with PyTechBrain library
from PyTechBrain import *
from time import sleep
from sys import exit as exit_application

print("Testing device.....")
# create object
my_board = PyTechBrain()

# just testing
data = my_board.list_devices_and_com_ports()
print(data)
my_board.full_debug_output()
