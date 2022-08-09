#!/bin/bash
sudo ./pytechbrain_eeprom_write
echo "=================[ ROZŁĄCZ płytkę i ENTER ]======="
read KK
python ./test_pth.py
