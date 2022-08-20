# Valid PyTechBrain methods:

```
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
```Valid methods:

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
