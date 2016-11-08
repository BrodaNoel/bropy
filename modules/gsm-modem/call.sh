#!/bin/bash

echo "Calling GSM-MODEM call.sh with arguments: $1 and $2 and $3"

# bropy call module gsm-modem sendsms "phone-number" "text"
DIR=`dirname $0`
gammu -c $DIR/gammu.config $1 TEXT $2 -text $3
exit $?