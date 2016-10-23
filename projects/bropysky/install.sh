#!/bin/bash
#
# 1 sola vez
sudo apt-get install -y gpsd

name='enable_uart'
value='0'
sudo sed -i "s/^\($name\s*=\s*\).*\$/\1$value/" /boot/config.txt

sudo systemctl stop serial-getty@ttyAMA0.service

# Al momento de ejecutar el RUN
#echo 'stty -F /dev/ttyAMA0 9600 -brkint -imaxbel' >> ~/.bash_profile
#echo 'sudo service gpsd stop' >> ~/.bash_profile
#echo 'sudo gpsd -n /dev/ttyAMA0 -F /var/run/gpsd.sock' >> ~/.bash_profile

echo 'BroPySky installed properly'
echo 'YOU MUST REBOOT THE RASPBERRY PI BEFORE CONTINUE!'
