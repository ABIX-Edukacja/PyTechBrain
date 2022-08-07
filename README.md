**PyTechBrain - innowacyjna nauka programowania**

Chciałbym przedstawić inspirację dla nauczycieli, w pełni zgodną z nową podstawą programową. To innowacyjny projekt - wprowadzający do tematu IoT.
Łączy elektronikę i programowanie w jednym pudełku, pozwala uczyć od klasy 4 szkoły podstawowej do końca liceum.
Zaczynamy środowiskiem opartym o Scratch, po czym przechodzimy do Pythona. Wszystko z czujnikami i diodami w tle...

PyTechBrain to nowa platforma wprowadzająca uczniów w dziedzinę IoT - Internet of Things (Internet Rzeczy).
Pozwala na nauczanie elektroniki i programowania w jednym. Jest w pełni zgodna z nową Podstawą Programową.
Łaczy prostotę wykonania i olbrzymie mozliwości nauczania programowania. Możemy wykorzystywać ją do budowania stacji pogodowych, podstaw inteligentnego miasta.  

Kompatybilny z Arduino UNO R3 i językiem Python

Pamiętaj - po podłączeniu zestawu USB do komputera standardowo urządzenie jest dostępne pod adresem /dev/ttyUSB0

### Minimalny kod w Python:

```python
print("This is sample of using PyTechBrain module.")
print("===========================================")

# creating board object with default debugging with no output
test_board = PyTechBrain()

# the same, but with full debugging during using module
# test_board = PyTechBrain(debug=True)

# Initializing board - first thing we need to do:
# automatic
# if test_board.board_init():
#     print("Super!")
# else:
#     print("Something went wrong... check output.")
#
# or manual
# if test_board.board_init("COM3"):
#     print("Super!")
# else:
#     print("Something went wrong... check output.")

# manual
if test_board.board_init():
    print("Super!")
    test_board.set_buzzer("beep")  # demo, on, off

    for _ in range(300):
        print(test_board.get_fotoresistor_raw())
        print(test_board.get_potentiometer_scale())
        print(test_board.get_temperature_celcius())
        print(test_board.get_volume_sensor_raw())
        s(0.1)

    test_board.set_rgb_red(255)
    s(0.2)
    test_board.set_rgb_red(0)
    test_board.set_rgb_green(255)
    s(0.2)
    test_board.set_rgb_green(0)
    test_board.set_rgb_blue(255)
    s(0.2)
    test_board.set_rgb_blue(0)
    s(0.2)
    test_board.set_pwm_diode(300)
    s(0.2)
    #
    test_board.set_signal_red("on")
    s(0.3)
    test_board.set_signal_yellow("on")
    s(0.3)
    test_board.set_signal_green("on")
    s(0.5)
    test_board.set_signal_red("off")
    s(0.3)
    test_board.set_signal_yellow("off")
    s(0.3)
    test_board.set_signal_green("off")
else:
    print("Something went wrong... check output.")

test_board.full_debug_output()
```

====================================================================
## Oprogramowanie i dokumentacja:

https://pytechbrain.edu.pl/oprogramowanie-zasoby.html

====================================================================

Standardowe metody:

```python
Valid methods:

    --[ general-purpose ]--
    P.license_info() -> str
    P.version_info() -> str
    P.debug_output() -> None (prints to screen)
    P.full_debug_output() -> None (prints to screen)
    P.usage_info() -> None (prints this text)

    --[ Output ]--
    P.set_rgb_red(power: int) ->  bool
    P.set_rgb_green(power: int) ->  bool
    P.set_rgb_blue(power: int) ->  bool
    P.set_rgb_color(color: tuple) -> bool
    -----------
    P.set_pwm_diode(power: int) -> bool
    -----------
    P.set_signal_red(state: str) -> bool
    P.set_signal_yellow(state: str) -> bool
    P.set_signal_green(state: str) -> bool
    -----------
    P.set_buzzer(type: str) -> None (plays tones)
        Different type of buzzer:
        "on" - turn on signal
        "off" - turn off signal
        "beep" - short (0.1 sec.) signal
        "demo" - music from Star Wars
    --[ Input ]--
    get_left_button_state(times=3) -> bool
    get_middle_button_state(times=3) -> bool
    get_right_button_state(times=3) -> bool
    times -> 3 ... 10 checks

    get_temperature_raw() -> int
    get_temperature_celcius() -> float (2 decimal precision)
    get_fotoresistor_raw() -> int
    get_volume_sensor_raw() -> int
    get_potentiometer_raw() -> int
    get_potentiometer_scale() -> float
```

==============================================================

W programie wykorzystano moduł pymata_aio (https://github.com/MrYsLab/pymata-aio) autorstwa Alan'a Yorinks'a (MrYsLab) oraz oprogramowanie firmowe do Arduino tego autora (https://github.com/MrYsLab/pymata-aio/tree/master/FirmataPlus).
