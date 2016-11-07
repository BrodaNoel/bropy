#! /usr/bin/python
import json
import os

f = open(os.path.dirname(os.path.realpath(__file__)) + '/../internals/test_data.json', 'r')
response = json.loads(f.read())

if isinstance(response['x'], int) and isinstance(response['y'], int) and isinstance(response['z'], int) :
	print "Looks like it's working well. Good news!"
else:
	print "Looks like it's is NOT working. Bad news!"
