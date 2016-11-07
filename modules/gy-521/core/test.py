#! /usr/bin/python
import json
import os

f = open(os.path.dirname(os.path.realpath(__file__)) + '/../internals/test_data.json', 'r')
response = json.loads(f.read())

if isinstance(response['temperature'], float) :
	print 'Temperature is working well. Good news!'
else:
	print "Looks like Temperature is NOT working. Bad news!"

if isinstance(response['accelerometer']['x'], float) and isinstance(response['accelerometer']['y'], float) and isinstance(response['accelerometer']['z'], float) :
	print 'Accelerometer is working well. Good news!'
else:
	print "Looks like Accelerometer is NOT working. Bad news!"

if isinstance(response['gyroscope']['x'], float) and isinstance(response['gyroscope']['y'], float) and isinstance(response['gyroscope']['z'], float) :
	print 'Gyroscope is working well. Good news!'
else:
	print "Looks like Gyroscope is NOT working. Bad news!"