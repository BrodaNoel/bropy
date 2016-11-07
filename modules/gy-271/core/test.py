#! /usr/bin/python
import json
import os

f = open(os.path.dirname(os.path.realpath(__file__)) + '/../internals/test_data.json', 'r')
response = json.loads(f.read())

if isinstance(response['x'], float) and isinstance(response['y'], float) and isinstance(response['z'], float) :
	print "Looks like it's working well. Good news!"
else:
	print "Looks like it's is NOT working. Bad news!"
