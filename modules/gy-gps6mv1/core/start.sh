#!/bin/bash

echo 'Starting GY-GPS6MV1 services'

stty -F /dev/ttyAMA0 9600 -brkint -imaxbel
sudo service gpsd stop
sudo gpsd -n /dev/ttyAMA0 -F /var/run/gpsd.sock
