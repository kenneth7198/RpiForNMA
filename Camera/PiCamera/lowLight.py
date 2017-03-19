import picamera
import time
import fractions

camera = picamera.PiCamera()
camera.resolution = (1280, 720)
camera.framerate = fractions.Fraction(1,6)
camera.shutter_speed = 6000000
camera.exposure_mode = 'off'
camera.ISO = 100
#time.sleep(10)

camera.capture('dark.jpg')
print('Finished')

