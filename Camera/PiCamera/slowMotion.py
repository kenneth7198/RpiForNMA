import picamera
import time

camera = picamera.PiCamera()
camera.resolution = (640,480)
camera.framerate = 90
camera.start_recording("slow.h264")
camera.wait_recording(1)
camera.stop_recording()

print("Finished")
