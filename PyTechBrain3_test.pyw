#!/usr/bin/env python3
# coding=utf-8
"""
 Copyright (c) 2018 Wiesław Rychlicki All rights reserved.
 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
 Version 3 as published by the Free Software Foundation; either
 or (at your option) any later version.
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.

 Program przeznaczony jest do testowania płytki edukacyjnej PyTechBrain
 według projektu Adama Jurkiewicza (http://pytechbrain.edu.pl/).

 W programie wykorzystano moduł pymata_aio (https://github.com/MrYsLab/pymata-aio)
 autorstwa Alan'a Yorinks'a (MrYsLab) oraz oprogramowanie firmowe do Arduino tego
 autora (https://github.com/MrYsLab/pymata-aio/tree/master/FirmataPlus).
 
"""

# Import modułu PyMata3 dla Python'a 3
from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants

# Import modułu interfejsu graficznego (GUI)
from tkinter import *

# Wykrywanie portu szeregowego, do którego przyłączono płytkę PyTechBrain.
# Potrzebne wyłącznie do wyświetlenia nazwy portu w interfejsie programu.

import serial.tools.list_ports

def portArduino():
    lists = list(serial.tools.list_ports.comports())
    lists = sorted(lists)
    for x in lists:
        if x[2].find('FTDI') != -1 or x[1].find('USB Serial Port') != -1:
            return x[0]
    return 'NULL'


# Nazwa portu (np. COM4)
port = portArduino()

# Utworzenie obiektu board (płytka) i automatyczna detekcja portu szeregowego.
board = PyMata3()

# Frame 1 - dioda RGB podłączona do pinów D3, D5 i D6 (PWM).

board.set_pin_mode(5, Constants.PWM)
board.set_pin_mode(3, Constants.PWM)
board.set_pin_mode(6, Constants.PWM)

def send_P_R(pwm_red):
    board.analog_write(5, int(pwm_red))
    LB_R.config(text = "~D5: "+pwm_red)
    
def send_P_G(pwm_green):
    board.analog_write(3, int(pwm_green))
    LB_G.config(text = "~D3: "+pwm_green)

def send_P_B(pwm_blue):
    board.analog_write(6, int(pwm_blue))
    LB_B.config(text = "~D6: "+pwm_blue)

# Frame 2 - buzzer podłączony do pinu D2.

def buzzer_on():
    board.play_tone(4, Constants.TONE_TONE, 440)
    LB1_2.config(text = "D4: ON")
    
def buzzer_off():
    board.play_tone(4, Constants.TONE_NO_TONE, 440)
    LB1_2.config(text = "D4: OFF")

# Frame 3 - biała dioda LED podłączona do pinu D9 (PWM).

board.set_pin_mode(9, Constants.PWM)

def send_PWM(pwm_pin9):
    board.analog_write(9, int(pwm_pin9))
    LB_PWM.config(text = "~D9: "+pwm_pin9)
    

# Frame 4 - model sygnalizatora drogowego 

#  Światło zielone - pin D2    
board.set_pin_mode(2, Constants.OUTPUT)
#  Światło żółte - pin D7 
board.set_pin_mode(7, Constants.OUTPUT)
#  Światło czerwone - pin D8 
board.set_pin_mode(8, Constants.OUTPUT)

def red():
    if var1.get() == 1:
        board.digital_write(8, 1)
        LB5.config(text = "D8: HIGH")
    else:
        board.digital_write(8, 0)
        LB5.config(text = "D8: LOW")

def yellow():
    if var2.get() == 1:
        board.digital_write(7, 1)
        LB6.config(text = "D7: HIGH")
    else:
        board.digital_write(7, 0)
        LB6.config(text = "D7: LOW")
        
def green():
    if var3.get() == 1:
        board.digital_write(2, 1)
        LB7.config(text = "D2: HIGH")
    else:
        board.digital_write(2, 0)
        LB7.config(text = "D2: LOW")

# Frame 5 - dioda LED (wbudowana) - pin D13.
        
board.set_pin_mode(13, Constants.OUTPUT)

def LED13_on():
    board.digital_write(13, 1)
    LB3_4.config(text = "D13: HIGH")
    
def LED13_off():
    board.digital_write(13, 0)
    LB3_4.config(text = "D13: LOW")


# Frame 6 - obsługa przycisków - piny D12, D11 i D10
# (w kolejności od lewej stromy do prawej)

board.set_pin_mode(10, Constants.INPUT)
board.set_pin_mode(11, Constants.INPUT)
board.set_pin_mode(12, Constants.INPUT)
board.enable_digital_reporting(10)
board.enable_digital_reporting(11)
board.enable_digital_reporting(12)

def poziom(p):
    if p:
        return('HIGH')
    else:
        return('LOW')
    
def read_buttons():
  def rb():
    temp = board.digital_read(12)
    lbl1.config(text='Przycisk A: '+str(temp))
    lbl1a.config(text='D12: '+str(poziom(temp)))
    temp = board.digital_read(11)
    lbl2.config(text='Przycisk B: '+str(temp))
    lbl2a.config(text='D11: '+str(poziom(temp)))
    temp = board.digital_read(10)
    lbl3.config(text='Przycisk C: '+str(temp))
    lbl3a.config(text='D10: '+str(poziom(temp)))
    lbl3.after(10, rb)
  rb()

# Frame 7 - odczytywanie danych z przetworników ADC
# - piny analogowe A2, A3, A4 i A5 (A0 i A1 - niewykorzystane).

# Pomiar natężenia światła - pin A2
board.set_pin_mode(2, Constants.ANALOG)
board.enable_analog_reporting(2)
# Pomiar natężenia dźwięku - pin A3
board.set_pin_mode(3, Constants.ANALOG)
board.enable_analog_reporting(3)
# Pomiar temperatury - pin A4
board.set_pin_mode(4, Constants.ANALOG)
board.enable_analog_reporting(4)
# Pomiar napięcia (z suwaka potencjometru) - pin A5
board.set_pin_mode(5, Constants.ANALOG)
board.enable_analog_reporting(5)

def read_analog():
  def ra():
    # Odczyt natężenia światła - pin analogowy A2.
    a2 = board.analog_read(2) # Wartość od 0 do 1023.
    str_a2 = 'Natężenie światła: {0:6.0f}%'.format(a2/1023.0*100)
    str_a2 += '\t\tA2: {0:5d}'.format(a2)
    lab_2.config(text=str_a2)
    
    # Odczyt natężenia dźwięku - pin analogowy A3.
    a3 = board.analog_read(3) # Wartość od 0 do 1023.
    str_a3 = 'Natężenie dźwięku:{0:5.0f}%'.format(a3/1023.0*100) 
    str_a3 += '\t\tA3: {0:5d}'.format(a3)
    lab_3.config(text=str_a3)

    # Odczyt temperatury - pin analogowy A4.
    a4 = board.analog_read(4) # Wartość od 0 do 1023.
    temp = a4 * 5 / 1023.0 / 2.45
    # 2.45 korekta wynikająca z użycia wzmacniacza - wartość może
    # być inna w każdej płytce (zależy od wartości użytych rezystorów)
    temp -= 0.5
    temp /= 0.01
    str_a4 = 'Temperatura: {0:8.1f} °C'.format(temp)  
    str_a4 += '\t\tA4: {0:5d}'.format(a4)
    lab_4.config(text=str_a4)

    # Odczyt ustawienia potencjometru - pin analogowy A5.
    a5 = board.analog_read(5) # Wartość od 0 do 1023.
    str_a5 = 'Potencjometr: {0:5.0f}%'.format(a5/1023.0*100)
    str_a5 += '\t\tA5: {0:5d}'.format(a5)
    lab_5.config(text=str_a5)
    lab_5.after(100, ra)
  ra()


# Główne okno programu.    
root = Tk()
root.geometry('530x500')
root.title('PyTechBrain3 - test')

# Budowanie interfejsu graficznego programu.

# Frame 1 - dioda RGB (PWM D5, D3 i D6).

labelframe1 = LabelFrame(root, text=" Dioda RGB ")
labelframe1.grid(column=0, row=0)
labelframe1.place(bordermode=OUTSIDE, x=10, y=10, height=150, width=250)
Label(labelframe1, text='RED  ').grid(column=0, row=0, sticky=W+S)
Label(labelframe1, text='GREEN').grid(column=0, row=1, sticky=W+S)
Label(labelframe1, text='BLUE ').grid(column=0, row=2, sticky=W+S)
pwm_red = Scale(labelframe1, from_=0, to=255, orient=HORIZONTAL, command=send_P_R)
pwm_red.grid(column=1, row=0)
LB_R = Label(labelframe1, text = "~D5: 0")
LB_R.grid(column=2, row=0, sticky=W+S)
pwm_green = Scale(labelframe1, from_=0, to=255, orient=HORIZONTAL, command=send_P_G)
pwm_green.grid(column=1, row=1)
LB_G = Label(labelframe1, text = "~D3: 0")
LB_G.grid(column=2, row=1, sticky=W+S)
pwm_blue = Scale(labelframe1, from_=0, to=255, orient=HORIZONTAL, command=send_P_B)
pwm_blue.grid(column=1, row=2)
LB_B = Label(labelframe1, text = "~D6: 0")
LB_B.grid(column=2, row=2, sticky=W+S)
# end - dioda RGB

# Frame 2 - buzzer (On/Off) - pin D4.

labelframe2 = LabelFrame(root, text=" Buzzer ")
labelframe2.grid(column=0, row=1)
labelframe2.place(bordermode=OUTSIDE, x=10, y=170, height=50, width=250)
B1 = Button(labelframe2, text ="On", command = buzzer_on)
B1.grid(column=0, row=0)
B1.place(bordermode=OUTSIDE, x=10, y=20, height=20, width=50)
B2 = Button(labelframe2, text ="Off", command = buzzer_off)
B2.grid(column=1, row=0)
B2.place(bordermode=OUTSIDE, x=70, y=20, height=20, width=50)
LB1_2 = Label(labelframe2, text = "D4: OFF")
LB1_2.grid(column=2, row=0)
LB1_2.place(bordermode=OUTSIDE, x=150, y=20, height=20, width=70)
# end buzzer

# Frame 3 - PWM, pin D9.

labelframe3 = LabelFrame(root, text=" PWM - pin D9 ")
labelframe3.grid(column=0, row=2)
labelframe3.place(bordermode=OUTSIDE, x=10, y=230, height=90, width=250)
Label(labelframe3, text='PWM  ').grid(column=0, row=0, sticky=W+S)
pwm_pin9 = Scale(labelframe3, from_=0, to=255, orient=HORIZONTAL, command=send_PWM)
pwm_pin9.grid(column=1, row=0)
LB_PWM = Label(labelframe3, text = "~D9: 0")
LB_PWM.grid(column=2, row=0, sticky=W+S)
# end - PWM

# Frame 4 - sygnalizator drogowy.

labelframe4 = LabelFrame(root, text=" Sygnalizator drogowy ")
labelframe4.grid(column=0, row=3)
labelframe4.place(bordermode=OUTSIDE, x=10, y=330, height=100, width=250)
var1 = IntVar()
Checkbutton(labelframe4, text="Red", variable=var1, command = red).grid(column=0, row=0, sticky=W)
LB5 = Label(labelframe4, text = "D8: LOW")
LB5.grid(column=1, row=0)
LB5.place(bordermode=OUTSIDE, x=150, y=20, height=20, width=70)
var2 = IntVar()
Checkbutton(labelframe4, text="Yellow", variable=var2, command = yellow).grid(column=0, row=1, sticky=W)
LB6 = Label(labelframe4, text = "D7: LOW")
LB6.grid(column=1, row=1)
LB6.place(bordermode=OUTSIDE, x=150, y=45, height=20, width=70)
var3 = IntVar()
Checkbutton(labelframe4, text="Green", variable=var3, command = green).grid(column=0, row=2, sticky=W)
LB7 = Label(labelframe4, text = "D2: LOW")
LB7.grid(column=1, row=2)
LB7.place(bordermode=OUTSIDE, x=150, y=70, height=20, width=70)
# end - sygnalizator drogowy

# Frame 5 - dioda LED, pin 13.

labelframe5 = LabelFrame(root, text=" Dioda LED13 ")
labelframe5.grid(column=0, row=4)
labelframe5.place(bordermode=OUTSIDE, x=10, y=440, height=50, width=250)
B3=Button(labelframe5, text ="On", command = LED13_on, width=50)
B3.grid(column=0, row=0, sticky=W+S)
B3.place(x=10, y=5, width=50, height=20)
B4 = Button(labelframe5, text ="Off", command = LED13_off, width=50)
B4.grid(column=1, row=0, sticky=W+S)
B4.place(x=70, y=5, width=50, height=20)
LB3_4 = Label(labelframe5, text = "D13: LOW")
LB3_4.grid(column=2, row=0, sticky=W+S)
LB3_4.place(x=150, y=5, height=20, width=70)
# end - LED13

# Frame 6 - przyciski (D10, D11 i D12).

labelframe6 = LabelFrame(root, text=" Wejścia cyfrowe (przyciski)")
labelframe6.grid(column=1, row=0)
labelframe6.place(bordermode=OUTSIDE, x=270, y=70, height=90, width=250)
lbl1 = Label(labelframe6, text = 'Przycisk A: 0')
lbl1.grid(column=0, row=0, sticky=W+S)
lbl1a = Label(labelframe6, text = 'D10: LOW')
lbl1a.grid(column=1, row=0, sticky=W+S)
lbl1a.place(x=150, y=0)
lbl2 = Label(labelframe6, text = 'Przycisk B: 0')
lbl2.grid(column=0, row=1, sticky=W+S)
lbl2a = Label(labelframe6, text = 'D11: LOW')
lbl2a.grid(column=1, row=1, sticky=W+S)
lbl2a.place(x=150, y=20)
lbl3 = Label(labelframe6, text = 'Przycisk C: 0')
lbl3.grid(column=0, row=2, sticky=W+S)
lbl3a = Label(labelframe6, text = 'D12: LOW')
lbl3a.grid(column=1, row=2, sticky=W+S)
lbl3a.place(x=150, y=40)
read_buttons()
# end - przyciski

# Frame 7 - wejścia analogowe (przetworniki ADC).

labelframe7 = LabelFrame(root, text=" Wejścia analogowe ")
labelframe7.grid(column=1, row=1)
labelframe7.place(bordermode=OUTSIDE, x=270, y=170, height=110, width=250)
lab_2 = Label(labelframe7, text = 'Analog A2: ')
lab_2.grid(column=0, row=2)
lab_2.place(x=0, y=0)
lab_3 = Label(labelframe7, text = 'Analog A3: ')
lab_3.grid(column=0, row=3)
lab_3.place(x=0, y=20)
lab_4 = Label(labelframe7, text = 'Analog A4: ')
lab_4.grid(column=0, row=4)
lab_4.place(x=0, y=40)
lab_5 = Label(labelframe7, text = 'Analog A5: ')
lab_5.grid(column=0, row=5)
lab_5.place(x=0, y=60)
read_analog()
# end - wejścia analogowe

# Frame 8 - informacje o projekcie i programie.

hardware = '\n***\nHardware: Adam Jurkiewicz\n'
hardware += '(pomysł i dystrybucja)\n'
hardware += 'https://cyfrowaszkola.waw.pl/'
software = '***\nSoftware: Wiesław Rychlicki\n'
software += 'https://github.com/wrata/PyTechBrain\n'
software += 'Wersja 2.0\n2018-12-04\n'
labelframe8 = LabelFrame(root, text=" O projekcie PyTechBrain ")
labelframe8.grid(column=1, row=2)
labelframe8.place(bordermode=OUTSIDE, x=270, y=290, height=200, width=250)
opis1 = Label(labelframe8, text = hardware)
opis1.grid(column=0, row=0)
opis2 = Label(labelframe8, text = software)
opis2.grid(column=0, row=2)
# end - informacje

# Frame 9 - port szeregowy wykrytego urządzenia.

labelframe9 = LabelFrame(root, text=" PyTechBrain at port ")
labelframe9.grid(column=1, row=3)
labelframe9.place(bordermode=OUTSIDE, x=270, y=10, height=50, width=250)
LB = Label(labelframe9, text = port)
LB.pack()
# end - port

root.mainloop()
