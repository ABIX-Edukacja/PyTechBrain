# testing functions
from PyTechBrain import *
from random import randint
from time import sleep

board = PyTechBrain(debug=True)

# ============[ tests ]======================

def test_device():
    print("TEST Init", "Success." if board.board_init() else "Failed.")

def test_signal_off():
    print("TEST Signal OFF", "Success." if board.set_off_outputs() else "Failed.")

def test_signal_on_off():
    tests = []
    tests.append(board.set_signal_red("on"))
    sleep(0.1)
    tests.append(board.set_signal_yellow("on"))
    sleep(0.1)
    tests.append(board.set_signal_green("on"))
    tests.append(board.set_buzzer("beep"))
    sleep(3)
    tests.append(board.set_off_outputs())
    print("TEST Signal state", "Success." if all(tests) else "Failed.")






if __name__ == '__main__':
    print(board.list_devices_and_com_ports())
    print("======[Starting testing...]=============")
    test_device()
    test_signal_off()
    test_signal_on_off()
