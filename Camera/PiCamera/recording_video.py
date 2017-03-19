import picamera

camera = picamera.PiCamera()
camera.resolution = (1280, 720)
camera.start_recording('my_video.h264')
camera.wait_recording(10)
camera.stop_recording()
