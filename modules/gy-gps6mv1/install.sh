#!/bin/bash

# Install dependencies
sudo apt-get install -y gpsd

# Disable UART
name='enable_uart'
value='0'
sudo sed -i "s/^\($name\s*=\s*\).*\$/\1$value/" /boot/config.txt

# Stop serial getty in ttyAMA0
sudo systemctl stop serial-getty@ttyAMA0.service

exit 0