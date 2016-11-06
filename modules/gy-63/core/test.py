#! /usr/bin/python
import json
import os

f = open(os.path.dirname(os.path.realpath(__file__)) + '/../internals/test_data.json', 'r')
response = json.loads(f.read())

if response['pressure'].isdigit() and response['temperature'].isdigit():
	print 'Everything is working well. Good news!'
else:
	print "Looks like it's NOT working. Bad news!"