#!/bin/bash

DIR=`dirname $0`

# Start module
$DIR/core/start.sh > /dev/null 2>&1

# Return the data
python $DIR/core/get.py

# Stop module
$DIR/core/stop.sh > /dev/null 2>&1