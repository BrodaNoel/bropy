#!/bin/bash

# Install dependencies
sudo apt-get install -y gammu

sudo touch /root/.gammurc
sudo echo '[gammu]' >> /root/.gammurc
sudo echo 'port = /dev/ttyUSB0' >> /root/.gammurc
sudo echo 'model = ' >> /root/.gammurc
sudo echo 'connection = at19200' >> /root/.gammurc
sudo echo 'synchronizetime = yes' >> /root/.gammurc
sudo echo 'logfile = ' >> /root/.gammurc
sudo echo 'logformat = nothing' >> /root/.gammurc
sudo echo 'use_locking = ' >> /root/.gammurc
sudo echo 'gammuloc = ' >> /root/.gammurc

exit 0