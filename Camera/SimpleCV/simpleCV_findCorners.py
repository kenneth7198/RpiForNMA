import SimpleCV

cam = SimpleCV.Camera()
disp = SimpleCV.Display()

while disp.isNotDone():
    img = cam.getImage()
    p = img.scale(320,240)
    s = p.findCorners()
    
    s.show()
    
