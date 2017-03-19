import SimpleCV

cam = SimpleCV.Camera()
disp = SimpleCV.Display()

while disp.isNotDone():
    img = cam.getImage()
    small = img.scale(320,240)
    small.show()
 
