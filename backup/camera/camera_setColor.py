from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

camera.resolution = (640, 480)
camera.start_preview()
for i in range(100):
    camera.annotate_text_size = 50
    camera.annotate_background = Color('blue')
    camera.annotate_foreground = Color('yellow')
    camera.contrast = i
    camera.annotate_text = "Hi Raspberry Pi! Contrast is : %s" % i
    sleep(0.1)
camera.stop_preview()
