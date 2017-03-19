import picamera

camera = picamera.PiCamera()

#camera.hflip=True
camera.vflip=True

camera.rotation=90
#camera.rotation=180
#camera.rotation=270
#camera.rotation=0

camera.start_preview()
camera.capture('img.jpg')
camera.stop_preview()
