#!/bin/bash
DIR=`dirname $0`
mkdir $DIR/internals
touch $DIR/internals/test_data.json

# Install dependencies
sudo apt-get install -y python-smbus

exit 0