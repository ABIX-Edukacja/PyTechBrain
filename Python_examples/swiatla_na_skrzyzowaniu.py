#!/usr/bin/env python3
#
# Kod źródłowy dla lekcji: Światła na skrzyżowaniu
# Autor: Adam Jurkiewicz, ABIX Edukacja https://pytechbrain.edu.pl 
#
#License:
#
#    This package is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This package is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this package; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA

from PyTechBrain import *
from time import sleep
uklad = PyTechBrain()

# na początku gasimy wszystkie światła
uklad.sygnalizator_czerwony('off')
uklad.sygnalizator_zolty('off')
uklad.sygnalizator_zielony('off')

while True:
    #zapala się czerwone
    uklad.sygnalizator_czerwony('on')
    sleep(1.7)
    uklad.sygnalizator_zolty('on')
    sleep(1.3)
    uklad.sygnalizator_czerwony('off')
    uklad.sygnalizator_zolty('off')
    uklad.sygnalizator_zielony('on')
    sleep(2.5)
    uklad.sygnalizator_zielony('off')
    uklad.sygnalizator_zolty('on')
    sleep(1.4)
    uklad.sygnalizator_zolty('off')