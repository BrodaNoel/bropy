#!/bin/bash

echo "Calling GSM-MODEM call.sh with arguments: $1 and $2 and $3"

# bropy call module gsm-modem sendsms "phone-number" "text"

sudo gammu $1 TEXT $2 -text $3
exit $?