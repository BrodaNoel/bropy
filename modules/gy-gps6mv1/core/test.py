#! /usr/bin/python
import json
import os

f = open(os.path.dirname(os.path.realpath(__file__)) + '/../internals/test_data.json', 'r')
response = json.loads(f.read())

if response['status'] == 'ok':
	print 'Everything is working well. Good news!'
elif response['status'] == 'error':
	print "Looks like it's not working. Error message:" + response['message']
else:
	print "Looks like it's NOT working AT ALL. Bad news!"