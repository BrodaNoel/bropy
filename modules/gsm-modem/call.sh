#!/bin/bash

# bropy call module gsm-modem sendsms "phone-number" "text"
DIR=`dirname $0`
gammu -c $DIR/gammu.config $1 TEXT $2 -text "$3"
exit $?