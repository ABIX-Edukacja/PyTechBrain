#!/bin/bash
# s2aio i potem Scratch 2 - offline bloki ABIX Edukacja
#
clear
cat << EOF
Teraz zostanie uruchomione oprogramowanie połączeniowe pomiędzy 
układem (c) PyTechBrain a programem (c) Scratch 2

Poczekaj chwilę, aż zobaczysz komunikat, że (c) PyTechBrain jest połączony.
=======================================
PRZYKŁAD: Using COM Port:/dev/ttyUSB0
======================================

Wtedy możesz uruchomić Scratch 2 i wczytać PyTechBrain_szablon.sb2
Po zakończonej pracy po prostu zamknij to okienko.
					ABIX Edukacja [www.abixedukacja.eu]
------------------------------------------------------------------------------
EOF
sleep 3
s2aio -c no_client 
echo " "
echo "---[ ERROR ]-----------------------"
echo "Jeśli to widzisz, to zmaksymalizuj okienko a potem "
echo "zrób PrintScreen i wyślij do : wsparcie@abixedukacja.eu"

read K
