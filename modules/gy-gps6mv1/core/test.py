#! /usr/bin/python
import json

f = open('./../internals/test_data.json', 'r')
response = json.loads(f.read())

if response.status == 'ok':
	print 'Everything is working well. Good news!'
else:
	print "Looks like it's not working. Bad news!"