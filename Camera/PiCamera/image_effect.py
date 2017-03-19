import picamera
import time

camera = picamera.PiCamera()

camera.resolution = (640, 480)
camera.start_preview()
camera.image_effect = 'colorswap'
time.sleep(2)
camera.capture('colorswap.jpg')
camera.stop_preview()
