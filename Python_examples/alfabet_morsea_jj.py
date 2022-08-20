# Kod źródłowy: https://pastebin.com/dpvsZgCQ
#
# Alfabet Morse'a - propozycja nauczyciela
# Autor: Jerzy Jasonek https://www.facebook.com/jerzy.jasonek
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
message = letter = ""
eng_to_morse = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    "?": "..--..",
    ",": "--..--",
}
inv_eng_to_morse = {eng_to_morse[k]: k for k in eng_to_morse}
print(eng_to_morse)

print(
    """
Please press buttons:

LEFT - RED - dot | RIGHT - GREEN - dash | MIDDLE - space | ORANGE - write message | POT max RIGHT - read message
"""
)


def check_letter(letter):
    if letter in inv_eng_to_morse:
        return inv_eng_to_morse[letter]
    else:
        print("X ", end="")
        return False


while True:
    dot = test_board.get_left_button_state(times=3)
    dash = test_board.get_right_button_state(times=3)
    space = test_board.get_middle_button_state(times=3)
    test_board.set_signal_yellow("on")

    potentiometer_value = test_board.get_potentiometer_raw()
    if potentiometer_value == 1023:
        test_board.set_signal_yellow("off")
        m = check_letter(letter)
        if m:
            message += m
        print()
        print("Message end - turn POT left and restart program")
        print(message)
        break

    if dot:
        test_board.set_signal_green("off")
        test_board.set_signal_red("on")
        print(".", end="")
        letter += "."
        test_board.set_buzzer("beep")
        sleep(0.2)
    elif dash:
        test_board.set_signal_red("off")
        test_board.set_signal_green("on")
        print("-", end="")
        letter += "-"
        test_board.set_buzzer("on")
        sleep(0.2)
        test_board.set_buzzer("off")
    elif space:
        if check_letter(letter):
            message += check_letter(letter)
        letter = ""
        print(" ", end="")
        sleep(0.2)
