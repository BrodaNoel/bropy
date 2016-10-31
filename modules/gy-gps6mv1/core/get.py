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

    while not gotData and attempts < 3:
      #It may take a second or two to get good data

      if gpsd.fix.latitude != 0 or gpsd.fix.longitude != 0:
        gotData = True
        attempts += 1

        output = '{'

        output += '{'
        output += 'latitude:', gpsd.fix.latitude, ','
        output += 'longitude:', gpsd.fix.longitude, ','
        output += 'time:"' + gpsd.fix.time + '",'
        output += 'utcTime:"' + gpsd.utc + '",'
        output += 'altitude:', gpsd.fix.altitude, ','
        output += 'eps:', gpsd.fix.eps, ','
        output += 'epx:', gpsd.fix.epx, ','
        output += 'epv:', gpsd.fix.epv, ','
        output += 'ept:', gpsd.fix.ept, ','
        output += 'speed:', gpsd.fix.speed, ','
        output += 'climb:', gpsd.fix.climb, ','
        output += 'track:', gpsd.fix.track, ','
        output += 'mode:', gpsd.fix.mode
        #print 'satellites:', gpsd.satellites
        output += '}'

        sys.stdout.write(output)
        
        sys.exit(0)

      else:
        time.sleep(1) #set to whatever

      if not gotData:
        sys.exit(1)

  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing