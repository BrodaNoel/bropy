#!/bin/bash
echo 'BroPySky installed properly'

# 1 sola vez
sudo apt-get install -y gpsd gpsd-clients
'enable_uart=0' dentro de /boot/config.txt
sudo reboot
sudo systemctl stop serial-getty@ttyAMA0.service

# al inicio
sudo stty -F /dev/ttyAMA0 9600 -brkint -imaxbel
sudo service gpsd stop
sudo gpsd -n /dev/ttyAMA0 -F /var/run/gpsd.sock

# Ver data
cgps -s
