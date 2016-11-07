import picamera
import os
import time

folder = os.path.dirname(os.path.realpath(__file__)) + '/../internals'
camera = picamera.PiCamera()

camera.sharpness = 0
camera.contrast = 0
camera.brightness = 50
camera.saturation = 0
camera.ISO = 0
camera.video_stabilization = False
camera.exposure_compensation = 0
camera.exposure_mode = 'auto'
camera.meter_mode = 'average'
camera.awb_mode = 'auto'
camera.image_effect = 'none'
camera.color_effects = None
camera.rotation = 0
camera.hflip = False
camera.vflip = False
camera.crop = (0.0, 0.0, 1.0, 1.0)

camera.capture(folder + '/test_photo.jpg')

camera.start_recording(folder + '/test_video.h264')
time.sleep(1)
camera.stop_recording()