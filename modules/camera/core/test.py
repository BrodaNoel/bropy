#! /usr/bin/python
import json
import os

photo = os.path.dirname(os.path.realpath(__file__)) + '/../internals/test_photo.jpg'
video = os.path.dirname(os.path.realpath(__file__)) + '/../internals/test_video.h264'

if os.path.isfile(photo)  :
	print 'Photo is working well. Good news!'
else:
	print 'Looks like Photo is NOT working. Bad news!'

if os.path.isfile(video)  :
	print 'Video is working well. Good news!'
else:
	print 'Looks like Video is NOT working. Bad news!'