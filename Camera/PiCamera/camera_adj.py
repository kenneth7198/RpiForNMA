import picamera
import time

camera = picamera.PiCamera()

camera.resolution = (640, 480)
camera.start_preview()
camera.brightness = 30
camera.contrast = 50
camera.exposure_mode = 'night'

time.sleep(2)

camera.capture('adj.jpg')
camera.stop_preview()
