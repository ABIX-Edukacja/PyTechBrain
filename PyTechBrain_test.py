# coding=utf-8
# To jest jeszcze wersja robocza ;)

import serial
import serial.tools.list_ports

# Python 3
from tkinter import *
# Python 2
# from Tkinter import *

from pyfirmata import Arduino, util
  
def portArduino():
    lists = list(serial.tools.list_ports.comports())
    lists = sorted(lists)
    for x in lists:
        if x[1].find('CH340') != -1 or x[1].find('Arduino') != -1 or x[1].find('FT231X') != -1 or x[2].find('FTDI') != -1:
            return x[0]
        
    return 'NULL'

port = portArduino()
board = Arduino(port)
it = util.Iterator(board)
it.start()

#frame 1
digital_5 = board.get_pin('d:5:p')
digital_3 = board.get_pin('d:3:p')
digital_6 = board.get_pin('d:6:p')

def send_P_R(pwm_red):
    digital_5.write(int(pwm_red)/255.0)
    LB_R.config(text = "~D5: "+pwm_red)
    
def send_P_G(pwm_green):
    digital_3.write(int(pwm_green)/255.0)
    LB_G.config(text = "~D3: "+pwm_green)

def send_P_B(pwm_blue):
    digital_6.write(int(pwm_blue)/255.0)
    LB_B.config(text = "~D6: "+pwm_blue)

#frame 2
digital_4 = board.get_pin('d:4:o')

def buzzer_on():
    digital_4.write(1)
    LB1_2.config(text = "D4: HIGH")
    
def buzzer_off():
    digital_4.write(0)
    LB1_2.config(text = "D4: LOW")

#frame 3
digital_9 = board.get_pin('d:9:p')

def send_PWM(pwm_pin9):
    digital_9.write(int(pwm_pin9)/255.0)
    LB_PWM.config(text = "~D9: "+pwm_pin9)

#frame 4
digital_2 = board.get_pin('d:2:o')
digital_7 = board.get_pin('d:7:o')
digital_8 = board.get_pin('d:8:o')

def red():
    if var1.get() == 1:
        digital_8.write(1)
        LB5.config(text = "D8: HIGH")
    else:
        digital_8.write(0)
        LB5.config(text = "D8: LOW")

def yellow():
    if var2.get() == 1:
        digital_7.write(1)
        LB6.config(text = "D7: HIGH")
    else:
        digital_7.write(0)
        LB6.config(text = "D7: LOW")
        
def green():
    if var3.get() == 1:
        digital_2.write(1)
        LB7.config(text = "D2: HIGH")
    else:
        digital_2.write(0)
        LB7.config(text = "D2: LOW")

#frame 5
digital_13 = board.get_pin('d:13:o')

def LED13_on():
    digital_13.write(1)
    LB3_4.config(text = "D13: HIGH")
    
def LED13_off():
    digital_13.write(0)
    LB3_4.config(text = "D13: LOW")

#frame 6
digital_10 = board.get_pin('d:10:i')
digital_11 = board.get_pin('d:11:i')
digital_12 = board.get_pin('d:12:i')
digital_10.enable_reporting()
digital_11.enable_reporting()
digital_12.enable_reporting()

def poziom(p):
    if p:
        return('HIGH')
    else:
        return('LOW')
    
def read_buttons():
  def rb():
    temp = digital_10.read()
    lbl1.config(text='Przycisk A: '+str(temp))
    lbl1a.config(text='D10: '+str(poziom(temp)))
    temp = digital_11.read()
    lbl2.config(text='Przycisk B: '+str(temp))
    lbl2a.config(text='D11: '+str(poziom(temp)))
    temp = digital_12.read()
    lbl3.config(text='Przycisk C: '+str(temp))
    lbl3a.config(text='D12: '+str(poziom(temp)))
    lbl3.after(10, rb)
  rb()

#frame 7
analog_0 = board.get_pin('a:0:i')
analog_1 = board.get_pin('a:1:i')
analog_2 = board.get_pin('a:2:i')
analog_3 = board.get_pin('a:3:i')
analog_4 = board.get_pin('a:4:i')
analog_5 = board.get_pin('a:5:i')
analog_0.enable_reporting()
analog_1.enable_reporting()
analog_2.enable_reporting()
analog_3.enable_reporting()
analog_4.enable_reporting()
analog_5.enable_reporting()

def read_analog():
  def ra():
    lab_0.config(text='Analog A0: '+str(int(1023*analog_0.read())))
    lab_1.config(text='Analog A1: '+str(int(1023*analog_1.read())))
    lab_2.config(text='Analog A2: '+str(int(1023*analog_2.read())))
    lab_3.config(text='Analog A3: '+str(int(1023*analog_3.read())))
    lab_4.config(text='Analog A4: '+str(int(1023*analog_4.read())))
    lab_5.config(text='Analog A5: '+str(int(1023*analog_5.read())))
    lab_5.after(100, ra)
  ra()
  
root = Tk()
root.geometry('530x500')
root.title('PyTechBrain - test')

# dioda RGB (PWM D5, D3 i D6)
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

# buzzer (On/Off) - pin D4
labelframe2 = LabelFrame(root, text=" Buzzer ")
labelframe2.grid(column=0, row=1)
labelframe2.place(bordermode=OUTSIDE, x=10, y=170, height=50, width=250)
B1 = Button(labelframe2, text ="On", command = buzzer_on)
B1.grid(column=0, row=0)
B1.place(bordermode=OUTSIDE, x=10, y=20, height=20, width=50)
B2 = Button(labelframe2, text ="Off", command = buzzer_off)
B2.grid(column=1, row=0)
B2.place(bordermode=OUTSIDE, x=70, y=20, height=20, width=50)
LB1_2 = Label(labelframe2, text = "D4: LOW")
LB1_2.grid(column=2, row=0)
LB1_2.place(bordermode=OUTSIDE, x=150, y=20, height=20, width=70)
# end buzzer

# PWM - pin D9
labelframe3 = LabelFrame(root, text=" PWM - pin D9 ")
labelframe3.grid(column=0, row=2)
labelframe3.place(bordermode=OUTSIDE, x=10, y=230, height=90, width=250)
Label(labelframe3, text='PWM  ').grid(column=0, row=0, sticky=W+S)
pwm_pin9 = Scale(labelframe3, from_=0, to=255, orient=HORIZONTAL, command=send_PWM)
pwm_pin9.grid(column=1, row=0)
LB_PWM = Label(labelframe3, text = "~D9: 0")
LB_PWM.grid(column=2, row=0, sticky=W+S)
# end - PWM

# sygnalizator drogowy
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

# dioda LED13 - pin 13
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

# przyciski (D10, D11 i D12)
labelframe6 = LabelFrame(root, text=" Wejścia cyfrowe (przyciski)")
labelframe6.grid(column=1, row=0)
labelframe6.place(bordermode=OUTSIDE, x=270, y=10, height=90, width=250)
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

# wejścia analogowe (przetworniki ADC)
labelframe7 = LabelFrame(root, text=" Wejścia analogowe ")
labelframe7.grid(column=1, row=1)
labelframe7.place(bordermode=OUTSIDE, x=270, y=110, height=150, width=250)
lab_0 = Label(labelframe7, text = 'Analog A0: '+str(int(1023*analog_0.read())))
lab_0.grid(column=0, row=0)
lab_1 = Label(labelframe7, text = 'Analog A1: '+str(int(1023*analog_1.read())))
lab_1.grid(column=0, row=1)
lab_2 = Label(labelframe7, text = 'Analog A2: '+str(int(1023*analog_2.read())))
lab_2.grid(column=0, row=2)
lab_3 = Label(labelframe7, text = 'Analog A3: '+str(int(1023*analog_3.read())))
lab_3.grid(column=0, row=3)
lab_4 = Label(labelframe7, text = 'Analog A4: '+str(int(1023*analog_4.read())))
lab_4.grid(column=0, row=4)
lab_5 = Label(labelframe7, text = 'Analog A5: '+str(int(1023*analog_5.read())))
lab_5.grid(column=0, row=5)
read_analog()
# end - wejścia analogowe

# informacje
hardware = '***\nHardware: Adam Jurkiewicz\n'
hardware += '(pomysł i dystrybucja)\n'
hardware += 'https://cyfrowaszkola.waw.pl/'
software = '***\nSoftware: Wiesław Rychlicki\n'
software += 'https://github.com/wrata/PyTechBrain\n'
labelframe8 = LabelFrame(root, text=" O projekcie PyTechBrain ")
labelframe8.grid(column=1, row=2)
labelframe8.place(bordermode=OUTSIDE, x=270, y=270, height=160, width=250)
opis1 = Label(labelframe8, text = hardware)
opis1.grid(column=0, row=0)
opis2 = Label(labelframe8, text = software)
opis2.grid(column=0, row=2)
# end - informacje

# wykryte urządzenie
labelframe9 = LabelFrame(root, text=" PyTechBrain at port ")
labelframe9.grid(column=1, row=3)
labelframe9.place(bordermode=OUTSIDE, x=270, y=440, height=50, width=250)
LB = Label(labelframe9, text = port)
LB.pack()
# end - urządzenie

root.mainloop()
