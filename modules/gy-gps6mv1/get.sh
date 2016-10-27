#!/bin/bash

# Start module
$("`dirname $0`/core/start.sh") > /dev/null 2>&1

# Return the data
$("python `dirname $0`/core/get.py")

# Stop module
$("`dirname $0`/core/stop.sh") > /dev/null 2>&1