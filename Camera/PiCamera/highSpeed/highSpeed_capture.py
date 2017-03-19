import picamera
import time

camera = picamera.PiCamera()
camera.resolution = (1280,720)
camera.framerate = 60
camera.ISO = 200
time.sleep(2)
camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g

camera.capture_sequence(['img%02d.jpg' % i for i in range(60)])

