import picamera
import time
import fractions

camera = picamera.PiCamera()
camera.resolution = (1280, 720)
camera.framerate = fractions.Fraction(1,6) #1/6fps
#camera.framerate = fractions.Fraction(1,3) #1/3fps 
#camera.framerate = 1
#camera.shutter_speed = 3000000 #3s
#camera.shutter_speed = 60000 #0.06s
#camera.shutter_speed = 600000 #0.6s
camera.shutter_speed =  6000000 #6s

camera.exposure_mode = 'off'
camera.ISO = 100
#time.sleep(10)

camera.capture('dark.jpg')
print('Finished')

