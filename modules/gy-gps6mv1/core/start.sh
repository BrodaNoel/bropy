#!/bin/bash

echo 'Starting GY-GPS6MV1 services'

# sudo stty -F /dev/ttyAMA0 9600 -brkint -imaxbel
sudo stty -F /dev/ttyAMA0 500:5:cbd:8a3b:3:1c:7f:15:4:0:1:0:11:13:1a:0:12:f:17:16:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0
sudo service gpsd stop
sudo gpsd -n /dev/ttyAMA0 -F /var/run/gpsd.sock
