import SimpleCV

cam = SimpleCV.Camera()
disp = SimpleCV.Display()

while disp.isNotDone():
    img = cam.getImage()
    img.save("img.jpg")  
    img.show()
