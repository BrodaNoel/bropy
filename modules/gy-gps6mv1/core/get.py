#! /usr/bin/python
# Written by Dan Mandle http://dan.mandle.me September 2012
# Modified by Broda Noel @brodanoel (in all social networks)
# License: GPL 2.0

from gps import *
from time import *
import time
import threading
import sys

gpsd = None #seting the global variable

class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true
 
  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer

if __name__ == '__main__':
  gpsp = GpsPoller() # create the thread
  try:
    gpsp.start() # start it up
    attempts = 0
    gotData = False

    while gotData == False and attempts < 3:
      #It may take a second or two to get good data

      if gpsd.fix.latitude != 0 or gpsd.fix.longitude != 0:
        gotData = True
        attempts += 1
        print '{'
        print 'latitude:', gpsd.fix.latitude, ','
        print 'longitude:', gpsd.fix.longitude, ','
        print 'time:"' + gpsd.fix.time + '",'
        print 'utcTime:"' + gpsd.utc + '",'
        print 'altitude:', gpsd.fix.altitude, ','
        print 'eps:', gpsd.fix.eps, ','
        print 'epx:', gpsd.fix.epx, ','
        print 'epv:', gpsd.fix.epv, ','
        print 'ept:', gpsd.fix.ept, ','
        print 'speed:', gpsd.fix.speed, ','
        print 'climb:', gpsd.fix.climb, ','
        print 'track:', gpsd.fix.track, ','
        print 'mode:', gpsd.fix.mode
        #print 'satellites:', gpsd.satellites
        print '}'
        sys.exit()
      else:
        time.sleep(1) #set to whatever

  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing