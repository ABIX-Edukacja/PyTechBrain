class PyTechBrain:
    """Działa z Python 3.6 i wyżej - płytka produkcji ABIX Edukacja
    Automatyczne wyszukiwanie płytki działa w Linux i Windows (sprawdzone)
    wówczas w ogóle nie trzeba nic podawać, lub możesz podać adres portu, np.:
    Linux - "/dev/ttyUSB0", MacOS - "/dev/cuaa01", Windows - "COM4"
    chętnych do współtworzenia kodu zapraszamy:
    https://pytechbrain.edu.pl | https://github.com/ABIX-Edukacja/PyTechBrain
    """

    __pytechbrain_version = "0.8.3"
    copyright_info = """
     Copyright (c) 2022 ABIX Edukacja - All rights reserved.
     This program is free software; you can redistribute it and/or
     modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
     Version 3 as published by the Free Software Foundation; either
     or (at your option) any later version.
     This program is distributed in the hope that it will be useful,
     but WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
     General Public License for more details.

     Program przeznaczony jest do płytki edukacyjnej PyTechBrain
     https://pytechbrain.edu.pl/

     W programie wykorzytypeo moduł pymata_aio (https://github.com/MrYsLab/pymata-aio)
     autorstwa Alan'a Yorinks'a (MrYsLab) oraz oprogramowanie firmowe do Arduino tego
     autora (https://github.com/MrYsLab/pymata-aio/tree/master/FirmataPlus)
    """

    @classmethod
    def license_info(cls) -> str:
        return cls.copyright_info

    @classmethod
    def version_info(cls) -> str:
        return cls.__pytechbrain_version

    def __init__(self, debug: bool = False) -> None:
        """If 'debug=True' then more info output to screen"""
        from sys import version, version_info

        self.debug = debug
        self.debug_init = f"Initializing object: {self}."
        self.debug_txt = [self.debug_init]
        self.last_debug_output = 0
        self.max_debug_info = 0
        self.__board_connected = False
        self.com_list = []
        self.arduino_port = None
        self.board = None
        self.__debug_add(f"Python version checking: \n{version}")
        print(self.debug_init)
        if self.debug:
            self.license_info()

    def board_init(self, search: str = "auto") -> bool:
        """Must be run as a first method after Init.
        search = "auto" - default value (automatic detection)
        search = Linux - "/dev/ttyUSB0", MacOS - "/dev/cuaa01", Windows - "COM4" (manual connect)
        """

        try:
            from pymata_aio.pymata3 import PyMata3
            from pymata_aio.constants import Constants
        except:
            raise ModuleNotFoundError("No PyMata3 module installed....")

        self.__debug_add(f"Board initialization starting - {search}.")
        if search == "auto":
            get_devices = self.__get_devices()
            get_arduino_port = self.__get_arduino_port()
            if get_devices and get_arduino_port:
                self.board = PyMata3(com_port=self.arduino_port)
                self.__board_connected = True
                self.__debug_add("Board initialization done.")
            else:
                self.__debug_add("Some errors with auto initialization.")
        else:
            try:
                self.arduino_port = search
                self.board = PyMata3(com_port=self.arduino_port)
                self.__board_connected = True
                self.__debug_add(f"Board at ({self.arduino_port}) initialization done.")
            except:
                self.__debug_add(
                    f"Some errors with manual ({self.arduino_port}) initialization."
                )

        self.debug_output()

        if self.__board_check():
            # input-output parameters
            # buttons
            self.button_left = 12
            self.button_middle = 11
            self.button_right = 10
            self.board.set_pin_mode(self.button_left, Constants.INPUT)
            self.board.set_pin_mode(self.button_middle, Constants.INPUT)
            self.board.set_pin_mode(self.button_right, Constants.INPUT)
            self.board.enable_digital_reporting(self.button_left)
            self.board.enable_digital_reporting(self.button_middle)
            self.board.enable_digital_reporting(self.button_right)
            # service_led
            self.service_led = 13
            self.board.set_pin_mode(self.service_led, Constants.OUTPUT)
            # pwm_diode
            self.pwm_diode = 9
            self.board.set_pin_mode(self.pwm_diode, Constants.PWM)
            # signal_rgb_3_leds
            self.red_diode = 8  # red
            self.yellow_diode = 7  # yellow
            self.green_diode = 2  # green
            self.board.set_pin_mode(self.red_diode, Constants.OUTPUT)
            self.board.set_pin_mode(self.yellow_diode, Constants.OUTPUT)
            self.board.set_pin_mode(self.green_diode, Constants.OUTPUT)
            # rgb_color - diode
            self.rgb_red = 5
            self.rgb_green = 3
            self.rgb_blue = 6
            self.board.set_pin_mode(self.rgb_red, Constants.PWM)
            self.board.set_pin_mode(self.rgb_green, Constants.PWM)
            self.board.set_pin_mode(self.rgb_blue, Constants.PWM)
            # buzzer
            self.buzzer = 4
            self.board.set_pin_mode(self.buzzer, Constants.OUTPUT)
            # analog sensors ...
            # empty -           = 0
            # empty -           = 1
            self.fotoresistor = 2
            self.volume_sensor = 3
            self.temp_sensor = 4
            self.potentiometer = 5
            self.board.set_pin_mode(self.fotoresistor, Constants.ANALOG)
            self.board.set_pin_mode(self.volume_sensor, Constants.ANALOG)
            self.board.set_pin_mode(self.temp_sensor, Constants.ANALOG)
            self.board.set_pin_mode(self.potentiometer, Constants.ANALOG)
            self.board.enable_analog_reporting(self.fotoresistor)
            self.board.enable_analog_reporting(self.volume_sensor)
            self.board.enable_analog_reporting(self.temp_sensor)
            self.board.enable_analog_reporting(self.potentiometer)
            # włączam raportowanie
            # self.it = util.Iterator(self.board)
            # self.it.start()
            self.__debug_add("All PINs are configured.")
            return True

        return False

    def __board_check(self) -> bool:
        return self.__board_connected

    def __get_arduino_port(self) -> bool:
        from sys import platform

        if self.com_list == []:
            self.__debug_add(f"COM list empty - break.")
            return False

        for val in self.com_list:
            if platform in ("linux", "darwin") and val.product == "ABIX_PyTechBrain":
                self.__debug_add(f"Found device at: {val.device}")
                self.arduino_port = val.device
                return True
            elif platform.startswith("win"):
                if val.manufacturer.startswith("FTDI") or val.description.startswith(
                    "USB Serial"
                ):
                    self.__debug_add(f"Found device at: {val.name}")
                    self.arduino_port = val.name
                    return True
            else:
                self.__debug_add(
                    f"Not Arduino FTDI compatible device: {val.description} / {val.manufacturer} / {val.usb_info()} "
                )
        else:
            self.__debug_add(f"Error - no FTDI compatible decise found.")
            return False

    def __debug_add(self, data: str) -> None:
        from datetime import datetime

        self.debug_txt.append(f"{datetime.now()} -> {data}")
        self.max_debug_info += 1

    def __get_devices(self) -> bool:
        from serial.tools import list_ports
        from sys import platform

        adapters = None
        adapters = list(list_ports.comports())
        for index, val in enumerate(adapters):
            if platform in ("linux", "darwin"):
                self.__debug_add(
                    f"Element {index}: {val.device} / {val.product} / {val.usb_description()}"
                )
            if platform.startswith("win"):
                self.__debug_add(
                    f"Element {index}: {val.description} / {val.manufacturer} / {val.usb_info()}"
                )
        if adapters:
            self.com_list = adapters
            return True
        else:
            self.__debug_add("No COM ports found with 'list_ports.comports()'!")
            return False

    def list_devices_and_com_ports(self) -> dict:
        from sys import platform, implementation
        from json import dumps
        import os

        devices = {
            "system": platform,
            "uname": str(os.uname())
            if platform in ("linux", "darwin")
            else "In Windows os.uname() does not working.",
            "python": str(implementation),
        }

        if not self.__get_devices():
            devices["COM"] = "No COM ports found."
            return dumps(devices, indent=2)

        for index, val in enumerate(self.com_list):
            devices[index] = [elem for elem in val]

        return dumps(devices, indent=2)

    def debug_output(self) -> None:
        if not self.debug:
            return None

        if not self.debug_txt or self.last_debug_output + 1 == self.max_debug_info:
            print("No new debug info")

        print("New debug messages:")
        new_messages = self.debug_txt[self.last_debug_output :]
        for message in new_messages:
            print(message)
            self.last_debug_output += 1

    def full_debug_output(self) -> None:
        print("All debug messages:")
        for message in self.debug_txt:
            print(message)

    def usage_info(self) -> None:
        print(
            f"""
This is a PyTechBrain: {self}
Initializing code:

    P = PyTechBrain(debug=False) # or True

    if P.board_init(search="auto"): # or 'COM3' or '/dev/ttyUSB0' or ...
        print("Super!")
    else:
        print("Something went wrong... check output.")
        test_board.full_debug_output()
        exit()

    # rest of code....
    # ....
    # ....

Valid methods:

    --[ general-purpose ]--
    P.license_info() -> str
    P.version_info() -> str
    P.debug_output() -> None (prints to screen)
    P.full_debug_output() -> None (prints to screen)
    P.usage_info() -> None (prints this text)
    P.list_devices_and_com_ports() -> dict (JSON)

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
    -----------
    P.set_off_outputs() -> boot
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
    -----------

        """
        )

    # ---[ Output functions]---
    def set_rgb_red(self, power: int) -> bool:
        """power - int 0..255"""
        assert (
            self.__board_connected == True
        ), "Board is not connected - do P.board_init() first!"
        if type(power) is not int:
            return False

        if power < 0:
            power = 0
        if power > 255:
            power = 255
        self.board.analog_write(self.rgb_red, power)
        return True

    def set_rgb_green(self, power: int) -> bool:
        """power - int 0..255"""
        assert (
            self.__board_connected == True
        ), "Board is not connected - do P.board_init() first!"
        if type(power) is not int:
            return False

        if power < 0:
            power = 0
        if power > 255:
            power = 255
        self.board.analog_write(self.rgb_green, power)
        return True

    def set_rgb_blue(self, power: int) -> bool:
        """power - int 0..255"""
        assert (
            self.__board_connected == True
        ), "Board is not connected - do P.board_init() first!"
        if type(power) is not int:
            return False

        if power < 0:
            power = 0
        if power > 255:
            power = 255
        self.board.analog_write(self.rgb_blue, power)
        return True

    def set_rgb_color(self, color: tuple) -> bool:
        """color - tuple (r,g,b)"""
        assert (
            self.__board_connected == True
        ), "Board is not connected - do P.board_init() first!"
        if type(color) is not tuple:
            return False

        for any in color:
            if type(any) is not int:
                return False

        ret = [False, False, False]
        ret[0] = self.set_rgb_red(color[0])
        ret[1] = self.set_rgb_green(color[1])
        ret[2] = self.set_rgb_blue(color[2])
        return True if all(ret) else False

    def set_pwm_diode(self, power: int) -> bool:
        """power - int 0..255"""
        assert (
            self.__board_connected == True
        ), "Board is not connected - do P.board_init() first!"
        if type(power) is not int:
            return False

        if power < 0:
            power = 0
        if power > 255:
            power = 255
        self.board.analog_write(self.pwm_diode, power)
        return True

    def set_signal_red(self, state: str) -> bool:
        """state - str 'on'  | 'off'"""
        assert (
            self.__board_connected == True
        ), "Board is not connected - do P.board_init() first!"
        if type(state) is not str:
            return False
        if state not in ("on", "off"):
            return False

        self.board.digital_write(self.red_diode, 1 if state == "on" else 0)
        return True

    def set_signal_yellow(self, state: str) -> bool:
        """state - str 'on'  | 'off'"""
        assert (
            self.__board_connected == True
        ), "Board is not connected - do P.board_init() first!"
        if type(state) is not str:
            return False
        if state not in ("on", "off"):
            return False

        self.board.digital_write(self.yellow_diode, 1 if state == "on" else 0)
        return True

    def set_signal_green(self, state: str) -> bool:
        """state - str 'on'  | 'off'"""
        assert (
            self.__board_connected == True
        ), "Board is not connected - do P.board_init() first!"
        if type(state) is not str:
            return False
        if state not in ("on", "off"):
            return False

        self.board.digital_write(self.green_diode, 1 if state == "on" else 0)
        return True

    def set_buzzer(self, sound_type: str) -> None:
        """Different type of buzzer:
        "on" - turn on signal
        "off" - turn off signal
        "beep" - short (0.1 sec.) signal
        "demo" - music from Star Wars"""
        from pymata_aio.constants import Constants
        from time import sleep

        assert (
            self.__board_connected == True
        ), "Board is not connected - do P.board_init() first!"
        if type(sound_type) is not str:
            return False
        if sound_type not in ("on", "off", "beep", "demo"):
            return False

        def note(f, t):
            """Note 'f' in 't' time"""
            self.board.play_tone(self.buzzer, Constants.TONE_TONE, f)
            sleep(t)
            self.board.play_tone(self.buzzer, Constants.TONE_NO_TONE, f)

        def play_star_wars():
            C0 = 16
            Db0 = 17
            D0 = 18
            Eb0 = 19
            E0 = 21
            F0 = 22
            Gb0 = 23
            G0 = 24
            Ab0 = 26
            A0 = 27
            Bb0 = 29
            B0 = 31
            C1 = 33
            Db1 = 35
            D1 = 37
            Eb1 = 39
            E1 = 41
            F1 = 44
            Gb1 = 46
            G1 = 49
            Ab1 = 52
            A1 = 55
            Bb1 = 58
            B1 = 62
            C2 = 65
            Db2 = 69
            D2 = 73
            Eb2 = 78
            E2 = 82
            F2 = 87
            Gb2 = 92
            G2 = 98
            Ab2 = 104
            A2 = 110
            Bb2 = 117
            B2 = 123
            C3 = 131
            Db3 = 139
            D3 = 147
            Eb3 = 156
            E3 = 165
            F3 = 175
            Gb3 = 185
            G3 = 196
            Ab3 = 208
            A3 = 220
            Bb3 = 233
            B3 = 247
            C4 = 262
            Db4 = 277
            D4 = 294
            Eb4 = 311
            E4 = 330
            F4 = 349
            Gb4 = 370
            G4 = 392
            Ab4 = 415
            A4 = 440
            Bb4 = 466
            B4 = 494
            C5 = 523
            Db5 = 554
            D5 = 587
            Eb5 = 622
            E5 = 659
            F5 = 698
            Gb5 = 740
            G5 = 784
            Ab5 = 831
            A5 = 880
            Bb5 = 932
            B5 = 988
            C6 = 1047
            Db6 = 1109
            D6 = 1175
            Eb6 = 1245
            E6 = 1319
            F6 = 1397
            Gb6 = 1480
            G6 = 1568
            Ab6 = 1661
            A6 = 1760
            Bb6 = 1865
            B6 = 1976
            C7 = 2093
            Db7 = 2217
            D7 = 2349
            Eb7 = 2489
            E7 = 2637
            F7 = 2794
            Gb7 = 2960
            G7 = 3136
            Ab7 = 3322
            A7 = 3520
            Bb7 = 3729
            B7 = 3951
            C8 = 4186
            Db8 = 4435
            D8 = 4699
            Eb8 = 4978

            # definicje czasów odgrywania nuta
            # define BPM 120    //  you can change this value changing all the others
            BPM = 120
            # define H 2*Q //half 2/4 and Q 60000/BPM //quarter 1/4
            Q = 60.0 / BPM
            H = 2 * Q
            # define E Q/2   //eighth 1/8
            E = Q / 2
            # define S Q/4 // sixteenth 1/16
            S = Q / 4
            # define W 4*Q // whole 4/4
            W = 4 * Q

            note(A3, Q)
            note(A3, Q)
            note(A3, Q)
            note(F3, E + S)
            note(C4, S)
            note(A3, Q)
            note(F3, E + S)
            note(C4, S)
            note(A3, H)
            note(E4, Q)
            note(E4, Q)
            note(E4, Q)
            note(F4, E + S)
            note(C4, S)
            note(Ab3, Q)
            note(F3, E + S)
            note(C4, S)
            note(A3, H)
            note(A4, Q)
            note(A3, E + S)
            note(A3, S)
            note(A4, Q)
            note(Ab4, E + S)
            note(G4, S)
            note(Gb4, S)
            note(E4, S)
            note(F4, E)
            sleep(E)
            note(Bb3, E)
            note(Eb4, Q)
            note(D4, E + S)
            note(Db4, S)
            note(C4, S)
            note(B3, S)
            note(C4, E)
            sleep(1 + E)
            note(F3, E)
            note(Ab3, Q)
            note(F3, E + S)
            note(A3, S)
            note(C4, Q)
            note(A3, E + S)
            note(C4, S)
            note(E4, H)
            note(A4, Q)
            note(A3, E + S)
            note(A3, S)
            note(A4, Q)
            note(Ab4, E + S)
            note(G4, S)
            note(Gb4, S)
            note(E4, S)
            note(F4, E)
            sleep(E)
            note(Eb4, Q)
            note(Bb3, E)
            note(D4, E + S)
            note(Db4, S)
            note(C4, S)
            note(B3, S)
            note(C4, E)
            sleep(E)
            note(F3, E)
            note(Ab3, Q)
            note(F3, E + S)
            note(C4, S)
            note(A3, Q)
            note(F3, E + S)
            note(C4, S)
            note(A3, H)
            sleep(2 * H)

        if sound_type == "on":
            self.board.play_tone(self.buzzer, Constants.TONE_TONE, 440)
        elif sound_type == "beep":
            self.board.play_tone(self.buzzer, Constants.TONE_TONE, 440)
            sleep(0.1)
            self.board.play_tone(self.buzzer, Constants.TONE_NO_TONE, 440)
        elif sound_type == "off":
            self.board.play_tone(self.buzzer, Constants.TONE_NO_TONE, 440)
        elif sound_type == "demo":
            self.__debug_add("Demo - playing Star Wars...")
            play_star_wars()

    def set_off_outputs(self) -> bool:
        assert (
            self.__board_connected == True
        ), "Board is not connected - do P.board_init() first!"

        ret = [False, False, False, False, False, False]
        ret[0] = self.set_rgb_color((0, 0, 0))
        ret[1] = self.set_pwm_diode(0)
        ret[2] = self.set_signal_red(0)
        ret[3] = self.set_signal_yellow(0)
        ret[4] = self.set_signal_green(0)
        ret[5] = self.set_buzzer("off")
        return True if all(ret) else False

    # ---[ Input ]---
    def get_left_button_state(self, times: int = 3) -> bool:
        """returns True if left button is pressed,
        defaults read 3 times, max 10"""
        assert (
            self.__board_connected == True
        ), "Board is not connected - do P.board_init() first!"
        if type(times) is not int:
            return False
        if times < 3 or times > 10:
            return False

        button_states = []
        for _ in range(times):
            button_states.append(self.board.digital_read(self.button_left))
        return any(button_states)

    def get_middle_button_state(self, times: int = 3) -> bool:
        """returns True if middle button is pressed,
        defaults read 3 times, max 10"""
        assert (
            self.__board_connected == True
        ), "Board is not connected - do P.board_init() first!"
        if type(times) is not int:
            return False
        if times < 3 or times > 10:
            return False

        button_states = []
        for _ in range(times):
            button_states.append(self.board.digital_read(self.button_middle))
        return any(button_states)

    def get_right_button_state(self, times: int = 3) -> bool:
        """returns True if right button is pressed,
        defaults read 3 times, max 10"""
        assert (
            self.__board_connected == True
        ), "Board is not connected - do P.board_init() first!"
        if type(times) is not int:
            return False
        if times < 3 or times > 10:
            return False

        button_states = []
        for _ in range(times):
            button_states.append(self.board.digital_read(self.button_right))
        return any(button_states)

    def get_temperature_raw(self) -> int:
        """returns raw value of temperature sensor - 0 ... 1023"""
        assert (
            self.__board_connected == True
        ), "Board is not connected - do P.board_init() first!"

        returned_value = self.board.analog_read(self.temp_sensor)
        return 0 if returned_value == None else returned_value

    def get_temperature_celcius(self) -> float:
        """returns value of temperature calculated to celcius"""
        assert (
            self.__board_connected == True
        ), "Board is not connected - do P.board_init() first!"

        raw_temp = self.get_temperature_raw()
        return float(round((raw_temp * 0.125) - 22, 2))

    def get_fotoresistor_raw(self) -> int:
        """returns raw value of fotoresistor sensor - 0 ... 1023"""
        assert (
            self.__board_connected == True
        ), "Board is not connected - do P.board_init() first!"

        returned_value = self.board.analog_read(self.fotoresistor)
        return 0 if returned_value == None else returned_value

    def get_volume_sensor_raw(self) -> int:
        """returns raw value of loud sensor - 0 ... 1023"""
        assert (
            self.__board_connected == True
        ), "Board is not connected - do P.board_init() first!"

        returned_value = self.board.analog_read(self.volume_sensor)
        return 0 if returned_value == None else returned_value

    def get_potentiometer_raw(self) -> int:
        """returns raw value of potentiometer sensor - 0 ... 1023"""
        assert (
            self.__board_connected == True
        ), "Board is not connected - do P.board_init() first!"

        returned_value = self.board.analog_read(self.potentiometer)
        return 0 if returned_value == None else returned_value

    def get_potentiometer_scale(self) -> float:
        """returns scaled value of potentiometer... -51 to +52"""
        assert (
            self.__board_connected == True
        ), "Board is not connected - do P.board_init() first!"

        raw_value = self.get_potentiometer_raw()
        return (raw_value - 511.5) / 10

    def full_reset(self) -> bool:
        """fully resets output to off"""
        assert (
            self.__board_connected == True
        ), "Board is not connected - do P.board_init() first!"
        outputs = []

        outputs.append(self.set_buzzer("off"))
        outputs.append(self.set_rgb_color((0, 0, 0)))
        outputs.append(self.set_signal_red("off"))
        outputs.append(self.set_signal_green("off"))
        outputs.append(self.set_signal_yellow("off"))
        outputs.append(self.set_pwm_diode(0))

        return all(outputs)


#########################
if __name__ == "__main__":
    from time import sleep as s
    import sys

    print("This is sample of using PyTechBrain module.")
    print("===========================================")

    # creating board object with default debugging with no output
    test_board = PyTechBrain()

    print(test_board.list_devices_and_com_ports())
    sys.exit(0)

    # the same, but with full debugging during using module
    # test_board = PyTechBrain(debug=True)

    # Initializing board - first thing we ned to do:
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
        # print("TEST")
        # s(2)
        # print("left - ", end=" ")
        # s(4)
        # print(test_board.get_left_button_state())
        #
        # test_board.set_buzzer("beep")  # demo, on, off
        # print("middle - ", end=" ")
        # s(4)
        # print(test_board.get_middle_button_state())
        #
        # test_board.set_buzzer("beep")  # demo, on, off
        # print("right - ", end=" ")
        # s(4)
        # print(test_board.get_right_button_state())

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
