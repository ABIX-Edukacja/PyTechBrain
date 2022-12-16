# Examples in Python for my board:

- Klasy 4-6: Wstęp: Obsługa SNAP (w tym zapis plików do chmury)

- Klasy 7-8: Wstęp: obsługa Mu-Editor (podstawy Python, instalacja bibliotek, PyPi)

Tematy lekcji wspólne dla obu poziomów (bloki + Python):
* światła na skrzyżowaniu - pętla nieskończona - ok
* tęcza budowana z kolorów RGB - pętla for i pętla nieskończona - pełna gama kolorów - ok
* kolory budowane z losowania: moduły standardowe (random, time) - ok
* Plotter z potencjometru + dioda PWM - ok
* kolory ustawiane przez przycisk + potencjometr - instrukcje warunkowe - ok
* alfabet morse'a w dwu wersjach:
* 1 - lewy klawisz kropka (czerwona dioda), środkowy klawisz kreska (zielony)
* 2 - tylko lewy klawisz
Praca w grupach: A koduje, B rozkodowuje.
** dla chętnych - zdanie pobierane z klawiatury i kodowane na morse'a - z jakimś czasem świecenia dla kropki i kreski.

Alarm temperatury (inteligentny dom) - sygnalizacja dźwiękowa przy przekroczonej temperaturze
** dla chętnych - różne kolory diody (RGB) w zależności od temperatury
Oświetlenie (inteligentny dom) - gdy ciemno, zapalamy diodę (np. zieloną)

Sterujemy siłą światła poprzez potencjometr - konwersja typów danych, skalowanie wartości.

Projekt dla chętnych w klasie 4-6: gra z wykorzystaniem przycisków, potencjometra.

Projekt dla klas 7-8: gra w pong'a (z książki) - potencjometr steruje jedną paletką.

Lo technikum: dodatkowo gra ponga i sterowanie, ale z dziedziczeniem klasy i dodaniem jakiejś własnej metody.


# Valid methods:

```
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
    P.get_left_button_state(times=3) -> bool
    P.get_middle_button_state(times=3) -> bool
    P.get_right_button_state(times=3) -> bool
    times -> 3 ... 10 checks

    P.get_temperature_raw() -> int
    P.get_temperature_celcius() -> float (2 decimal precision)
    P.get_fotoresistor_raw() -> int
    P.get_volume_sensor_raw() -> int
    P.get_potentiometer_raw() -> int
    P.get_potentiometer_scale() -> float
```
