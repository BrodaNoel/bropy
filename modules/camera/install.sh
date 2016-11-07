#!/bin/bash
DIR=`dirname $0`
mkdir $DIR/internals

# Install dependencies
sudo apt-get install -y python-picamera

exit 0